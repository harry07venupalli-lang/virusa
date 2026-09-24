import java.util.*;
public class QuizServiceTest {
    public static void main(String[] args){
        List<Question> q=List.of(
            new Question(1,"2+2?",new String[]{"3","4","5","6"},1,"Math"),
            new Question(2,"Java is a...",new String[]{"DB","Language","Browser","OS"},1,"Java"),
            new Question(3,"SQL is used to...",new String[]{"Query data","Draw","Video","Compile"},0,"SQL"));
        QuizResult r=new QuizService(q).evaluate("Test",new int[]{1,0,-1});
        if(r.getCorrectAnswers()!=2||r.getWrongAnswers()!=0||r.getUnanswered()!=1||r.getScore()!=2) throw new AssertionError("Quiz evaluation test failed");
        System.out.println("All QuizService tests passed.");
    }
}