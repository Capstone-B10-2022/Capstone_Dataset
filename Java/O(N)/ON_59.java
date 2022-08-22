// Source: https://www.geeksforgeeks.org/rearrange-array-maximum-minimum-form/

// Java program to rearrange an array in minimum
// maximum form
 
import java.util.Arrays;
 
public class ON_59
{
    // Prints max at first position, min at second position
    // second max at third position, second min at fourth
    // position and so on.
    static void rearrange(int[] arr, int n)
    {
        // Auxiliary array to hold modified array
        int temp[] = arr.clone();
 
        // Indexes of smallest and largest elements
        // from remaining array.
        int small = 0, large = n - 1;
 
        // To indicate whether we need to copy remaining
        // largest or remaining smallest at next position
        boolean flag = true;
 
        // Store result in temp[]
        for (int i = 0; i < n; i++) {
            if (flag)
                arr[i] = temp[large--];
            else
                arr[i] = temp[small++];
 
            flag = !flag;
        }
    }
 
    // Driver code
    public static void main(String[] args)
    {
        int arr[] = new int[] { 1, 2, 3, 4, 5, 6 };
 
        System.out.println("Original Array ");
        System.out.println(Arrays.toString(arr));
 
        rearrange(arr, arr.length);
 
        System.out.println("Modified Array ");
        System.out.println(Arrays.toString(arr));
    }
}
