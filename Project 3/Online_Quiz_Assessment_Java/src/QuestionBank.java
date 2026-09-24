import java.io.*;
import java.nio.file.*;
import java.util.*;

public class QuestionBank {
    private final Path file;
    public QuestionBank(Path file){this.file=file;}
    public List<Question> loadQuestions() throws IOException{
        List<Question> questions=new ArrayList<>();
        if(!Files.exists(file)) return questions;
        try(BufferedReader reader=Files.newBufferedReader(file)){
            String line;
            while((line=reader.readLine())!=null){
                if(line.isBlank()||line.startsWith("#")) continue;
                String[] p=line.split("\\|",-1);
                if(p.length!=8) continue;
                int id=Integer.parseInt(p[0]);
                String[] options={p[3],p[4],p[5],p[6]};
                questions.add(new Question(id,p[2],options,Integer.parseInt(p[7]),p[1]));
            }
        }
        return questions;
    }
    public void addQuestion(Question q)throws IOException{
        Files.createDirectories(file.getParent());
        String[] o=q.getOptions();
        try(BufferedWriter w=Files.newBufferedWriter(file,StandardOpenOption.CREATE,StandardOpenOption.APPEND)){
            w.write(q.getId()+"|"+clean(q.getCategory())+"|"+clean(q.getText())+"|"+clean(o[0])+"|"+clean(o[1])+"|"+clean(o[2])+"|"+clean(o[3])+"|"+q.getCorrectOption());
            w.newLine();
        }
    }
    private String clean(String s){return s.replace("|","/").replace("
"," ").replace(""," ");}
}