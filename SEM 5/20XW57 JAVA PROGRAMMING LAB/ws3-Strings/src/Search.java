//problem
//        Write a program to search a string for a specified character or substring.

import java.util.Scanner;

public class Search {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        System.out.printf("Enter the String:\n");
        String InputString = input.nextLine();
        System.out.printf("Enter the String to be searched:\n");
        String SearchString = input.nextLine();

        for(int i=0;i<InputString.length();i++){
            if(InputString.charAt(i)==SearchString.charAt(0)){
                System.out.printf("The required string is found!\n");
                for (int j=i;j<i+SearchString.length();j++){
                    System.out.printf("%c",InputString.charAt(j));
                }
                break;
            }
            if(i==InputString.length()-1){
                System.out.printf("String not found.");
            }
        }
    }
}
