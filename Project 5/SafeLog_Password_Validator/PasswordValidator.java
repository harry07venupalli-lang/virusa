import java.util.Scanner;

public class PasswordValidator {
    public static boolean isValidPassword(String password) {
        boolean hasUppercase=false, hasDigit=false;
        for(int i=0;i<password.length();i++){
            char ch=password.charAt(i);
            if(Character.isUpperCase(ch)) hasUppercase=true;
            if(Character.isDigit(ch)) hasDigit=true;
        }
        return password.length()>=8&&hasUppercase&&hasDigit;
    }
    public static void showFeedback(String password){
        boolean hasUppercase=false,hasDigit=false;
        for(int i=0;i<password.length();i++){
            char ch=password.charAt(i);
            if(Character.isUpperCase(ch)) hasUppercase=true;
            if(Character.isDigit(ch)) hasDigit=true;
        }
        if(password.length()<8) System.out.println("Too short. Password must contain at least 8 characters.");
        if(!hasUppercase) System.out.println("Missing an uppercase letter.");
        if(!hasDigit) System.out.println("Missing a digit.");
    }
    public static void main(String[] args){
        Scanner scanner=new Scanner(System.in);
        while(true){
            System.out.print("\nEnter your password: ");
            String password=scanner.nextLine();
            if(isValidPassword(password)){
                System.out.println("Password is valid!");
                System.out.println("Strong password accepted.");
                break;
            }
            System.out.println("Password is invalid.");
            showFeedback(password);
            System.out.println("Please try again.");
        }
        scanner.close();
    }
}
