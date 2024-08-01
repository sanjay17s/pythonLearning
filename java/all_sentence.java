package java;
import java.util.Scanner;

public class all_sentence {
    public static void main(String[] args) {
        System.out.print("Enter your sentence here: ");
        Scanner sc = new Scanner(System.in);
        String sentence = sc.nextLine();
        System.out.println(toTitle(sentence));
        
    }

    public static String toTitle(String sentence) {
        StringBuilder s = new StringBuilder();
        boolean first_word=true;

        for(char character : sentence.toCharArray()) {
            if(Character.isLetter(character)){
                if(first_word) {
                    s.append(Character.toUpperCase(character));
                    first_word =false;
                }
                else{
                    s.append(character);
                }
            }
            else {
                s.append(character);
                first_word=true;
            }
        }

        return s.toString();
}
}
