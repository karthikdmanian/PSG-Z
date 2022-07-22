
public class Sixth {
    public static void main(String[] args) {
        int[] arr = new int[]{7,4,8,2,9};
        System.out.printf("No of buildings that can see sunset: %d",findSunsetBuildings(arr));
     }

     public static int findSunsetBuildings(int[] arr){
        int pivot=arr[0];
        System.out.printf("%d\n",pivot);
        int count=1;
         for (int i = 0; i < arr.length; i++) {
             if(arr[i]>pivot) {
                 System.out.printf("%d\n",arr[i]);
                 count++;
             }
         }

        return count;
     }
}
