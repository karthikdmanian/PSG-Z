import java.util.Scanner;

public class AdjacentCharacters {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        System.out.println("Enter the string .");
        String str = input.nextLine();
//        mutable string
        StringBuilder newStr = new StringBuilder(str.length()*2);
        for (int i = 0; i < str.length()-1; i++) {
            if(str.charAt(i)==str.charAt(i+1)){
                newStr.append(str.charAt(i));
                newStr.append('*');
            }
            else{
                newStr.append(str.charAt(i));
            }
        }
        newStr.append(str.charAt(str.length()-1));
        System.out.println(newStr);
    }
}
