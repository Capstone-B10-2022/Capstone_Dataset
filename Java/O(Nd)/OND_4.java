// Java program for the above approach
import java.io.*;
import java.lang.*;
import java.util.*;
 
class OND_4 {
 
    // Function to check if two matrices
    // are equal or not
   static Boolean isEqual(int[ ][ ] arr, int[ ][ ] brr)
    {
        int n = arr.length;
        int m = arr[0].length;
 
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (arr[i][j] != brr[i][j])
                    return false;
            }
        }
 
        return true;
    }
 
    // Function to rotate matrix by 90 degrees clockwise
    static void rotate(int [ ][ ] m)
    {
        int n = m.length;
 
        for (int i = 0; i < n; i++)
            for (int j = 0; j < i; j++){
                      //swap
                      int temp = m[i][j];
                      m[i][j] = m[j][i];
                      m[j][i] = temp;
            }
 
        for (int i = 0; i < n; i++)
           Collections.reverse(Arrays.asList(m[i]));
    }
 
    // Find Minimum rotation to reach the desired matrix
    static void findRotation(int[ ][ ] arr,  int[ ][ ] brr)
    {
 
        if (isEqual(arr, brr) == true) {
            System.out.print("0");
              return;
        }
 
        for (int i = 1; i < 4; i++) {
 
            // Rotate by 90 degrees clockwise
            rotate(arr);
 
            // Checking if both arr[][] and brr[]
            // are now equal or not
            if (!isEqual(arr, brr)) {
                if (i < 4 - i) {
                  System.out.print("+" + i );
                }
                else
                      System.out.print("-" + (4 - i));
                return;
            }
        }
 
        // If converting brr[][] is not possible
        System.out.print("NA");
    }
 
    // Driver Code
    public static void main (String[] args) {
 
        int [ ][ ] arr = { { 2, 3 }, { 4, 5 } };
        int [ ][ ] brr = { { 4, 2 }, { 5, 3 } };
       
        // Function Call
        findRotation(arr, brr);
    }
}
