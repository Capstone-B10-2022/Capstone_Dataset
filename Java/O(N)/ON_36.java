// Java program for above approach
import java.util.*;
class ON_36{
 
// Function to find no of iterations
static int minZero(int A[], int n)
{
 
    // Initialize count c = 0
    int c = 0;
 
    // If 0 already in array return c
 
    if (Arrays.stream(A).min().getAsInt()== 0)
        return c;
 
    // Iterate till we get zero in array
    while (Arrays.stream(A).min().getAsInt() != 0) {
 
        // Assign first element in x
        int x = A[0];
 
        // Loop to subtract consecutive element
        for (int i = 0; i < (n - 1); i++) {
            A[i] = Math.abs(A[i] - A[i + 1]);
        }
        A[n - 1] = Math.abs(A[n - 1] - x);
 
        // Increment count c
        c += 1;
    }
 
    // Return c
    return c;
}
 
// Driver Code
public static void main(String[] args)
{
   
    // Original array
    int arr[] = { 2, 6, 3, 4, 8, 7 };
 
    // Length of array
    int N = arr.length;
 
    // calling function
    int x = minZero(arr, N);
 
    // print the result
    System.out.print(x);
}
 
}

