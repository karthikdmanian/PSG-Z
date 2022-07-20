import java.util.Scanner;

public class RollNo {
    public static void Main(String[] args){
        Scanner input = new Scanner(System.in);
        int Regno = input.nextInt();
        int n;
        int black=Regno;
        int count;
        for(count=0;black>0;count++){
            black=black/2;
        }
        n=count;
        System.out.println(n);
    }
}
