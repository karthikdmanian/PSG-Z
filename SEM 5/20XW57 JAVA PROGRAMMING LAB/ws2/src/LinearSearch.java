import java.util.Scanner;

public class LinearSearch {
    public static void main(String[] args){
        int[] arr;
        System.out.println("Enter the number of elements in array");
        Scanner input = new Scanner(System.in);
        int n = input.nextInt();
        arr = new int[n];
        System.out.println("Enter the array elements:");
        for (int i = 0; i < n; i++) {
            arr[i]=input.nextInt();
        }
        printArray(arr);
        System.out.printf("Enter the element to be searched:");
        int x= input.nextInt();
        System.out.printf("The element is in the array : %b",LinearSearch(arr,x));
    }
    public static void printArray(int[] arr){
        for(int i=0;i<arr.length;i++){
            System.out.printf("%d",arr[i]);
        }
    }

    public static boolean LinearSearch(int[] arr,int elt) {
        for (int i = 0; i < arr.length; i++) {
            if (arr[i] == elt) {
                return true;
            }
        }
        return false;
    }
}
