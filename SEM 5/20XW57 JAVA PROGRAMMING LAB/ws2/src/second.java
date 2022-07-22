public class second {
    public static void main(String[] args) {

        int[] arr = new int[]{1,2,3,4,5,6,7};

        System.out.printf("The Original array is:\n");
        printArray(arr);
        System.out.printf("The rotated array is:\n");
        arr = rotate(arr,2);
        printArray(arr);

    }
    public static int[] rotate(int[] arr,int d){
        int[] rotatedArray = new int[arr.length];
        for (int i = 0; i < arr.length; i++) {
            rotatedArray[i]=arr[(i+d)%arr.length];
        }
        return rotatedArray;
    }
    public static void printArray(int[] arr){
        for(int i=0;i<arr.length;i++){
            System.out.printf("%d",arr[i]);
        }
    }
}
