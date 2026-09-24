import java.util.*;

public class QuizService {
    private final List<Question> questions;
    public QuizService(List<Question> questions){this.questions=new ArrayList<>(questions);}
    public List<Question> getQuestions(){return new ArrayList<>(questions);}
    public QuizResult evaluate(String userName,int[] answers){
        int correct=0,wrong=0,unanswered=0;
        for(int i=0;i<questions.size();i++){
            int answer=i<answers.length?answers[i]:-1;
            if(answer==-1) unanswered++;
            else if(answer==questions.get(i).getCorrectOption()) correct++;
            else wrong++;
        }
        int score=correct;
        double percentage=questions.isEmpty()?0:correct*100.0/questions.size();
        String performance;
        if(percentage>=90) performance="Excellent";
        else if(percentage>=75) performance="Very Good";
        else if(percentage>=60) performance="Good";
        else if(percentage>=40) performance="Needs Improvement";
        else performance="Keep Practicing";
        return new QuizResult(userName,questions.size(),correct,wrong,unanswered,score,percentage,performance);
    }
}