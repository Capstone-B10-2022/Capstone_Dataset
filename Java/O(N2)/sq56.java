// Java implementation to print
// the counter clock wise
// spiral traversal of matrix
//https://www.geeksforgeeks.org/print-given-matrix-counter-clock-wise-spiral-form/
import java.io.*;

class sq56
{
	static int R = 4;
	static int C = 4;

	// function to print the
	// required traversal
	static void counterClockspiralPrint(int Matrix[][])
	{
		int size = R;
		int i = size, k = 0, flag = 0, j = 0;
	
		// Print all layers one by one
		while (i > 0) {
	
			// Print First Column of Current Layer
			for (j = flag; j < i; j++) {
				System.out.print(Matrix[j][k]+" ");
			}
			i = i - 1;
			j = j - 1;
			k = j;
	
			// Print bottom row and last column
			// of current layer
			if (i > 0) {
				for (j = size - i; j < i + 1; j++)
					System.out.print(Matrix[k][j]+" ");
				for (j = k - 1; j > size - i - 2; j--)
					System.out.print(Matrix[j][k]+" ");
			}
			else
				break;
			j = j + 1;
			k = j;
			i = i - 1;
	
			// Print top row of current layer
			if (i > 0) {
				for (j = i; j > size - i - 2; j--)
					System.out.print(Matrix[k][j]+" ");
				k = k + 1;
				i = i + 1;
				flag = flag + 1;
			}
			else
				break;
		}
	}
	
	// Driver Code
	public static void main(String[] args)
	{
		int Matrix[][] = { { 1, 2, 3, 4 },
						{ 5, 6, 7, 8 },
						{ 9, 10, 11, 12 },
						{ 13, 14, 15, 16 } };
		
		// Function calling		
		counterClockspiralPrint(Matrix);
	}
}

// This code is contributed by shruti456rawal
