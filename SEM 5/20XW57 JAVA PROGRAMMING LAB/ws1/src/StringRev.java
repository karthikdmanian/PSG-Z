import java.util.Scanner;

public class StringRev {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        System.out.printf("Enter the string: ");
        String inputString = input.nextLine();
        String rev="";
        //rev
        for (int i = 0; i < inputString.length(); i++) {
            char ch = inputString.charAt(i);
            rev = ch + rev;
        }
        System.out.printf("The Reversed string is %s\n",rev);
        int count =0;
        for (int i=0; i<inputString.length();i++){
            if(inputString.charAt(i)==rev.charAt(i)){
                count++;
            }
        }
        System.out.printf("%d",count);
    }
}
