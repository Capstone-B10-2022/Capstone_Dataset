// Java Implementation of Right Rotation 
// of an Array K number of times
import java.util.*;
import java.lang.*;
import java.io.*;
  
class ON_42
{
  
// Function to rightRotate array
static void RightRotate(int a[], 
                        int n, int k)
{
      
    // If rotation is greater 
    // than size of array
    k=k%n;
  
    for(int i = 0; i < n; i++)
    {
        if(i<k)
        {
            // Printing rightmost 
            // kth elements
            System.out.print(a[n + i - k] 
                             + " ");
        }
        else
        {
            // Prints array after
            // 'k' elements
            System.out.print(a[i - k] 
                             + " ");
        }
    }
    System.out.println();
}
      
// Driver program
public static void main(String args[])
{
    int Array[] = {1, 2, 3, 4, 5};
    int N = Array.length;
  
    int K = 2;
    RightRotate(Array, N, K);
  
}
}