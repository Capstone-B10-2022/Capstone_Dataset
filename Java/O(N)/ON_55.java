// Source: https://www.geeksforgeeks.org/reorder-a-array-according-to-given-indexes/


//Java to find positions of zeroes flipping which
// produces maximum number of consecutive 1's
 
import java.util.Arrays;
 
class ON_55
{
    static int arr[] = new int[]{50, 40, 70, 60, 90};
    static int index[] = new int[]{3,  0,  4,  1,  2};
     
    // Method to reorder elements of arr[] according
    // to index[]
    static void reorder()
    {
        int temp[] = new int[arr.length];
      
        // arr[i] should be present at index[i] index
        for (int i=0; i<arr.length; i++)
            temp[index[i]] = arr[i];
      
        // Copy temp[] to arr[]
        for (int i=0; i<arr.length; i++)
        {
           arr[i]   = temp[i];
           index[i] = i;
        }
    }
     
    // Driver method to test the above function
    public static void main(String[] args)
    {
         
        reorder();
         
        System.out.println("Reordered array is: ");
        System.out.println(Arrays.toString(arr));
        System.out.println("Modified Index array is:");
        System.out.println(Arrays.toString(index));
         
    }
}
