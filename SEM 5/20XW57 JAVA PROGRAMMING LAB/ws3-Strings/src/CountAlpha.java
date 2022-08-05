//problem
//        Write a program inputs a line of text and uses String method to determine the total number of occurrences of
//        each letter of the alphabet in the text. Uppercase and lowercase letters should be counted together. Store the
//        totals for each letter in an array, and print the values in tabular format after the totals have been determined.

import java.util.Locale;
import java.util.Scanner;

public class CountAlpha {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        System.out.printf("Enter the String:\n");
        String InputString = input.nextLine();

        String str = InputString.toLowerCase(Locale.ROOT);
//        System.out.printf("%s",str);

        int[] arr = new int[26];

        for(int i=0;i<str.length();i++){
            if(str.charAt(i)-'a'>=0 && str.charAt(i)-'a'<26) {
                arr[str.charAt(i) - 'a']++;
            }
        }

        for(int j=0;j<arr.length;j++){
            System.out.printf("%c - %d \n",'a'+j,arr[j]);
        }
    }
}
