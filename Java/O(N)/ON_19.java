/*package whatever //do not write package name here */
 
import java.io.*;
import java.util.Arrays;
class ON_19 {
    public static void leftRotate(int[] A, int a, int k)
    {
      //if the value of k ever exceeds the length of the array
        int c = k % a;
       
      //initializing array D so that we always
      //have a clone of the original array to rotate
        int[] D = A.clone();
       
        rotateArray(D, 0, c - 1);
        rotateArray(D, c, a - 1);
        rotateArray(D, 0, a - 1);
       
      // printing the rotates array
        System.out.print(Arrays.toString(D));
        System.out.println();
    }
   
  // Function to rotate the array from start index to end index
    public static int[] rotateArray(int[] A, int start,
                                    int end)
    {
        while (start < end) {
            int temp = A[start];
            A[start] = A[end];
            A[end] = temp;
            start++;
            end--;
        }
        return A;
    }
 
    // Driver Code
    public static void main(String[] args)
    {
        int A[] = { 1, 3, 5, 7, 9 };
        int n = A.length;
 
        int k = 2;
        leftRotate(A, n, k);
 
        k = 3;
        leftRotate(A, n, k);
 
        k = 4;
        leftRotate(A, n, k);
    }
}
