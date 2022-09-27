// Java program to shift k elements in a
// matrix.
//https://www.geeksforgeeks.org/shift-matrix-elements-k/
import java.io.*;
import java.util.*;

public class sq55 {
	
	static int N = 4;
	
	// Function to shift first k elements
	// of each row of matrix.
	static void shiftMatrixByK(int [][]mat,
									int k)
	{
		if (k > N) {
			System.out.print("Shifting is"
						+ " not possible");
			return;
		}
		
		int j = 0;
		while (j < N) {
			
			// Print elements from index k
			for (int i = k; i < N; i++)
				System.out.print(mat[j][i] + " ");
				
			// Print elements before index k
			for (int i = 0; i < k; i++)
				System.out.print(mat[j][i] + " ");
				
			System.out.println();
			j++;
		}
	}
	
	// Driver code
	public static void main(String args[])
	{
		int [][]mat = new int [][]
					{ {1, 2, 3, 4},
					{5, 6, 7, 8},
					{9, 10, 11, 12},
					{13, 14, 15, 16} };
		int k = 2;
		
		// Function call
		shiftMatrixByK(mat, k);
	}
}

// This code is contributed by Manish Shaw
// (manishshaw1)
