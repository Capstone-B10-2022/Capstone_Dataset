// Java implementation for print left
// rotation of any array K times
import java.io.*;
import java.util.*;
 
class ON_26{
     
// Function for the k times left rotation
static void leftRotate(Integer arr[], int k,
                                      int n)
{
   
     // In Collection class rotate function
     // takes two parameters - the name of
     // array and the position by which it
     // should be rotated
     // The below function will be rotating
     // the array left  in linear time
      
     // Collections.rotate()rotate the
     // array from right hence n-k
    Collections.rotate(Arrays.asList(arr), n - k);
     
    // Print the rotated array from start position
    for(int i = 0; i < n; i++)
        System.out.print(arr[i] + " ");
}
 
// Driver code
public static void main(String[] args)
{
    Integer arr[] = { 1, 3, 5, 7, 9 };
    int n = arr.length;
    int k = 2;
     
    // Function call
    leftRotate(arr, k, n);
}
}
