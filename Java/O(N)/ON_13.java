import java.util.Arrays;
 
public class ON_13
{
    static int arr[] = new int[]{1, 2, 3, 4, 5};
     
    
    static void rotate()
    {
       int i = 0, j = arr.length - 1;
       while(i != j)
       {
         int temp = arr[i];
         arr[i] = arr[j];
         arr[j] = temp;
         i++;
       }
    }
     
    /* Driver program */
    public static void main(String[] args)
    {
        System.out.println("Given Array is");
        System.out.println(Arrays.toString(arr));
         
        rotate();
         
        System.out.println("Rotated Array is");
        System.out.println(Arrays.toString(arr));
    }
}
