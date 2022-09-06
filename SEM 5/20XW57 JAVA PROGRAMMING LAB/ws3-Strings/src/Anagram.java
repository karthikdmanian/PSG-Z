import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class Anagram {

    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        boolean exists = true;
        System.out.printf("Enter the first string :");
        String string1 = input.nextLine();
        System.out.printf("Enter the next string :");
        String string2 = input.nextLine();

        List<Character> charlist = new ArrayList<Character>();

        for (int i = 0; i < string1.length(); i++) {
            charlist.add(string1.charAt(i));
        }

        for (int i = 0; i < string2.length(); i++) {
            for (int j = 0; j < charlist.size() ; j++) {
                    if(string2.charAt(i)==charlist.get(j)){
                        exists=true;
                        charlist.remove(j);
                    }
            }
        }

        if (charlist.size()>0){
            System.out.printf("Not a anagram.");
        }
        else{
            System.out.printf("Anagram . ");
        }
    }
}
