//problem
//        Program to print smallest and biggest possible palindrome word in a given string
import java.util.Locale;
import java.util.Scanner;

public class Palindrome
{
    public static boolean isPalindrome(String str){
//        codde
        return false;
    }

    public static void main(String[] args)
    {
//        inputs
        Scanner input = new Scanner(System.in);
        System.out.printf("Enter the String:\n");
        String InputString = input.nextLine();

//        max and min length
        int small = Integer.MAX_VALUE;
        int large = Integer.MIN_VALUE;
        String smallP="";
        String largeP="";

        String str = InputString.toLowerCase(Locale.ROOT)+' ';
        String word="";
        String[] words = new String[30];
        int count=0;
        for (int i = 0; i < str.length(); i++)
        {
            if(str.charAt(i)!=' ')
            {
                word+=str.charAt(i);
            }
            else{
                words[count]=word;
                count+=1;
                word="";
            }
        }

        for(int i=0; i<count; i++){
            System.out.printf("%s\n",words[i]);
            if(isPalindrome(words[i])){
                if(words[i].length()<small){
                    small=words[i].length();
                    smallP=words[i];
                }
                if(words[i].length()>large){
                    large=words[i].length();
                    largeP=words[i];
                }
            }
        }
    }
}
