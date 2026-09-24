public class QuizResult {
    private final String userName;
    private final int totalQuestions,correctAnswers,wrongAnswers,unanswered,score;
    private final double percentage;
    private final String performance;
    public QuizResult(String userName,int totalQuestions,int correctAnswers,int wrongAnswers,int unanswered,int score,double percentage,String performance){
        this.userName=userName;this.totalQuestions=totalQuestions;this.correctAnswers=correctAnswers;this.wrongAnswers=wrongAnswers;this.unanswered=unanswered;this.score=score;this.percentage=percentage;this.performance=performance;
    }
    public String getUserName(){return userName;} public int getTotalQuestions(){return totalQuestions;}
    public int getCorrectAnswers(){return correctAnswers;} public int getWrongAnswers(){return wrongAnswers;}
    public int getUnanswered(){return unanswered;} public int getScore(){return score;}
    public double getPercentage(){return percentage;} public String getPerformance(){return performance;}
}