// Java Program to find the
// count of rotations
public class ON_32 {
  
    // Function to return the count of
    // rotations
    public static int countRotation(int[] arr,
                                    int n)
    {
        for (int i = 1; i < n; i++) {
            // Find the smallest element
            if (arr[i] < arr[i - 1]) {
                // Return its index
                return i;
            }
        }
        // If array is not
        // rotated at all
        return 0;
    }
  
    // Driver Code
    public static void main(String[] args)
    {
        int[] arr1 = { 4, 5, 1, 2, 3 };
  
        System.out.println(
            countRotation(
                arr1,
                arr1.length));
    }
}