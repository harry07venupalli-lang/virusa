import java.io.*;
import java.nio.file.*;
import java.util.*;

public class QuizApp {
    private static final Path QUESTION_FILE=Path.of("data","questions.txt");
    private static final int TIME_LIMIT_SECONDS=60;
    public static void main(String[] args){
        Scanner sc=new Scanner(System.in);
        try{
            QuestionBank bank=new QuestionBank(QUESTION_FILE);
            while(true){
                System.out.println("\n======================================");
                System.out.println("       ONLINE QUIZ & ASSESSMENT");
                System.out.println("======================================");
                System.out.println("1. Take Quiz");
                System.out.println("2. Admin - Add Question");
                System.out.println("3. Exit");
                System.out.print("Choose an option: ");
                String choice=sc.nextLine().trim();
                if(choice.equals("1")) takeQuiz(sc,bank.loadQuestions());
                else if(choice.equals("2")) addQuestion(sc,bank);
                else if(choice.equals("3")){System.out.println("Goodbye!");return;}
                else System.out.println("Invalid choice.");
            }
        }catch(Exception e){System.out.println("Application error: "+e.getMessage());}
        finally{sc.close();}
    }
    private static void takeQuiz(Scanner sc,List<Question> qs){
        if(qs.isEmpty()){System.out.println("No questions found.");return;}
        System.out.print("\nEnter your name: "); String name=sc.nextLine().trim();
        if(name.isEmpty()) name="Guest";
        int[] answers=new int[qs.size()]; Arrays.fill(answers,-1);
        long deadline=System.currentTimeMillis()+TIME_LIMIT_SECONDS*1000L;
        System.out.println("\nQuiz started! Total time: "+TIME_LIMIT_SECONDS+" seconds.");
        System.out.println("Enter 1-4, or press Enter to skip.");
        for(int i=0;i<qs.size();i++){
            long left=(deadline-System.currentTimeMillis())/1000;
            if(left<=0){System.out.println("\nTime is up!");break;}
            Question q=qs.get(i);
            System.out.println("\n--------------------------------------");
            System.out.println("Question "+(i+1)+"/"+qs.size()+" | Time left: "+left+" sec");
            System.out.println("["+q.getCategory()+"] "+q.getText());
            for(int j=0;j<4;j++) System.out.println((j+1)+". "+q.getOptions()[j]);
            System.out.print("Your answer: ");
            String input=sc.nextLine().trim();
            if(System.currentTimeMillis()>=deadline){System.out.println("Time expired.");break;}
            if(!input.isEmpty()){
                try{int a=Integer.parseInt(input);if(a>=1&&a<=4)answers[i]=a-1;else System.out.println("Invalid answer; marked unanswered.");}
                catch(NumberFormatException e){System.out.println("Invalid answer; marked unanswered.");}
            }
        }
        QuizResult r=new QuizService(qs).evaluate(name,answers);
        System.out.println("\n======================================");
        System.out.println("             QUIZ RESULT");
        System.out.println("======================================");
        System.out.println("Name: "+r.getUserName());
        System.out.println("Total Questions: "+r.getTotalQuestions());
        System.out.println("Correct: "+r.getCorrectAnswers());
        System.out.println("Wrong: "+r.getWrongAnswers());
        System.out.println("Unanswered: "+r.getUnanswered());
        System.out.println("Score: "+r.getScore()+"/"+r.getTotalQuestions());
        System.out.printf("Percentage: %.2f%%%n",r.getPercentage());
        System.out.println("Performance: "+r.getPerformance());
    }
    private static void addQuestion(Scanner sc,QuestionBank bank)throws IOException{
        try{
            List<Question> existing=bank.loadQuestions();
            System.out.println("\n========== ADMIN: ADD QUESTION ==========");
            System.out.print("Question ID: "); int id=Integer.parseInt(sc.nextLine().trim());
            for(Question q:existing) if(q.getId()==id){System.out.println("That ID already exists.");return;}
            System.out.print("Category: ");String category=sc.nextLine();
            System.out.print("Question: ");String text=sc.nextLine();
            String[] options=new String[4];
            for(int i=0;i<4;i++){System.out.print("Option "+(i+1)+": ");options[i]=sc.nextLine();}
            System.out.print("Correct option (1-4): ");int correct=Integer.parseInt(sc.nextLine())-1;
            new AdminService(QUESTION_FILE).addQuestion(new Question(id,text,options,correct,category));
            System.out.println("Question added successfully.");
        }catch(NumberFormatException e){System.out.println("Invalid number.");}
        catch(IllegalArgumentException e){System.out.println("Could not add question: "+e.getMessage());}
    }
}