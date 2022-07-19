import java.util.Scanner;

public class KeyGenerator {
    public static void arrayprint(int[] arr){
        for (int i = 0; i < arr.length; i++) {
            System.out.printf("%d ",arr[i]);
        }
    }

    public static int keyGen(int[] arr){
        //thousands
        int minT=9,maxH=0,minTen=9,maxOne=0;
        for (int i = 0; i < arr.length; i++) {
            if(arr[i]/1000<minT){
                minT=arr[i]/1000;
            }
            if((arr[i]/100)%10>maxH){
                maxH=(arr[i]/100)%10;
            }
            if((arr[i]/10)%10<minTen){
                minTen=(arr[i]/10)%10;
            }
            if(arr[i]%10>maxOne){
                maxOne=arr[i]%10;
            }
        }
        return minT*1000+maxH*100+minTen*10+maxOne;
    }
    public static void main(String[] args) {
        //inputs
        Scanner input = new Scanner(System.in);
        System.out.printf("Enter the three numbers with space:\n");
        String inputString = input.nextLine();
        String[] arr= inputString.split(" ");
        //arrayinput
        int[] numbers;
        numbers = new int[3];

        for (int i = 0; i < arr.length; i++) {
            numbers[i]=Integer.parseInt(arr[i]);
        }

        System.out.println(keyGen(numbers));
    }

}
