// Java program for the above approach
import java.io.*;
import java.lang.*;
import java.util.*;
 
public class ON3_2 {
 
    // Function to print the matrix
    static void print(int mat[][])
    {
        // Iterate over the rows
        for (int i = 0; i < mat.length; i++) {
 
            // Iterate over the columns
            for (int j = 0; j < mat[0].length; j++)
 
                // Print the value
                System.out.print(mat[i][j] + " ");
           
            System.out.println();
        }
    }
 
    // Function to perform the swapping of
    // matrix elements in clockwise manner
    static void performSwap(int mat[][], int i, int j)
    {
        int N = mat.length;
 
        // Stores the last row
        int ei = N - 1 - i;
 
        // Stores the last column
        int ej = N - 1 - j;
 
        // Perform the swaps
        int temp = mat[i][j];
        mat[i][j] = mat[ej][i];
        mat[ej][i] = mat[ei][ej];
        mat[ei][ej] = mat[j][ei];
        mat[j][ei] = temp;
    }
 
    // Function to rotate non - diagonal
    // elements of the matrix K times in
    // clockwise direction
    static void rotate(int mat[][], int N, int K)
    {
        // Update K to K % 4
        K = K % 4;
 
        // Iterate until K is positive
        while (K-- > 0) {
 
            // Iterate each up to N/2-th row
            for (int i = 0; i < N / 2; i++) {
 
                // Iterate each column
                // from i to N - i - 1
                for (int j = i; j < N - i - 1; j++) {
 
                    // Check if the element
                    // at i, j is not a
                    // diagonal element
                    if (i != j && (i + j) != N - 1) {
 
                        // Perform the swapping
                        performSwap(mat, i, j);
                    }
                }
            }
        }
 
        // Print the matrix
        print(mat);
    }
   
    // Driver Code
    public static void main(String[] args)
    {
 
        int K = 5;
        int mat[][] = {
            { 1, 2, 3, 4 },
            { 6, 7, 8, 9 },
            { 11, 12, 13, 14 },
            { 16, 17, 18, 19 },
        };
       
        int N = mat.length;
        rotate(mat, N, K);
    }
}
