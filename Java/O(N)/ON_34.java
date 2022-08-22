// Java program of the above approach
import java.util.*;
class ON_34{
  
// Function that prints maximum
// equal elements
static void maximumEqual(int a[], 
                         int b[], int n)
{
  
    // Vector to store the index
    // of elements of array b
    int store[] = new int[(int) 1e5];
  
    // Storing the positions of
    // array B
    for (int i = 0; i < n; i++) 
    {
        store[b[i]] = i + 1;
    }
  
    // frequency array to keep count
    // of elements with similar
    // difference in distances
    int ans[] = new int[(int) 1e5];
  
    // Iterate through all element in arr1[]
    for (int i = 0; i < n; i++)
    {
  
        // Calculate number of
        // shift required to
        // make current element
        // equal
        int d = Math.abs(store[a[i]] - (i + 1));
  
        // If d is less than 0
        if (store[a[i]] < i + 1) 
        {
            d = n - d;
        }
  
        // Store the frequency
        // of current diff
        ans[d]++;
    }
  
    int finalans = 0;
  
    // Compute the maximum frequency
    // stored
    for (int i = 0; i < 1e5; i++)
        finalans = Math.max(finalans,
                            ans[i]);
  
    // Printing the maximum number
    // of equal elements
    System.out.print(finalans + " ");
}
  
// Driver Code
public static void main(String[] args)
{
    // Given two arrays
    int A[] = { 6, 7, 3, 9, 5 };
    int B[] = { 7, 3, 9, 5, 6 };
  
    int size = A.length;
  
    // Function Call
    maximumEqual(A, B, size);
}
}
