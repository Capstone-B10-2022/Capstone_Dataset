// Java implementation for the above approach
import java.util.*;
 
class ON_31{
 
    // Initialize the array
   static int[] Array = { 1, 2, 3, 4, 5 };
    
   static void reverse( int start, int end) {
 
       // Temporary variable to store character
       int temp;
       while (start <= end)
       {
          
           // Swapping the first and last character
           temp = Array[start];
           Array[start] = Array[end];
           Array[end] = temp;
           start++;
           end--;
       }
   }
   
// Function to rotate the array
// to the right, K times
static void RightRotate( int K)
{
    int n = Array.length;
 
    // Case when K > N or K < -N
    K = K < 0 ? ((K * -1) % n) * -1 : K % n;
 
    // Case when K is negative
    K = K < 0 ? (n - (K * -1)) : K;
 
    // Reverse all the array elements
    reverse(0, n-1);
 
    // Reverse the first k elements
    reverse(0, n - K);
 
    // Reverse the elements from K
    // till the end of the array
    reverse( K, n-1);
}
 
// Driver code
public static void main(String[] args)
{
 
 
    // Find the size of the array
    int N = Array.length;
 
    // Initialize K
    int K = -2;
 
    // Call the function and
    // print the answer
    RightRotate(K);
 
    // Print the array after rotation
    for (int i = 0; i < N; i++) {
 
        System.out.print(Array[i]+ " ");
    }
 
    System.out.println();
}
}