
public class Third {
    public static void main(String[] args) {
        int[] arr = new int[]{12,35,1,10,34,1};
        System.out.printf("the second largest element in the array is %d",findSecondLargestElement(arr));
    }
    public static int findSecondLargestElement(int[] arr){
        int SL=-Integer.MAX_VALUE+1;
        int max=-Integer.MAX_VALUE;
        for (int i = 0; i < arr.length; i++) {
            if(arr[i]>SL){
                if(arr[i]==findLargestElement(arr)){
                    continue;
                }
                else{
                    SL=arr[i];
                }
            }
        }
        return SL;
    }
    public static int findLargestElement(int[] arr){
        int L=-Integer.MAX_VALUE;
        for (int i = 0; i < arr.length; i++) {
            if(arr[i]>L){
                    L=arr[i];
            }
        }
        return L;
    }
}
