public class Question {
    private final int id;
    private final String text;
    private final String[] options;
    private final int correctOption;
    private final String category;

    public Question(int id,String text,String[] options,int correctOption,String category){
        this.id=id; this.text=text; this.options=options; this.correctOption=correctOption; this.category=category;
    }
    public int getId(){return id;}
    public String getText(){return text;}
    public String[] getOptions(){return options;}
    public int getCorrectOption(){return correctOption;}
    public String getCategory(){return category;}
}