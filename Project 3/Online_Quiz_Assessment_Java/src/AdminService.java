import java.io.IOException;
import java.nio.file.Path;

public class AdminService {
    private final QuestionBank bank;
    public AdminService(Path file) { bank = new QuestionBank(file); }
    public void addQuestion(Question q) throws IOException {
        for (Question old : bank.loadQuestions())
            if (old.getId() == q.getId()) throw new IllegalArgumentException("Question ID already exists.");
        if (q.getOptions().length != 4) throw new IllegalArgumentException("Exactly 4 options are required.");
        if (q.getCorrectOption() < 0 || q.getCorrectOption() > 3) throw new IllegalArgumentException("Correct option must be 1-4.");
        bank.addQuestion(q);
    }
}