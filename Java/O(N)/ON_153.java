// Source: https://www.geeksforgeeks.org/squares-of-matrix-diagonal-elements/

// Efficient JAVA program to print squares of
// diagonal elements.
import java.io.*;

class ON_153
{
	static int MAX =100;
	
	// function of diagonal square
	static void diagonalsquare(int mat[][], int row, int column)
	{
		// This loop is for finding of square of
		// the first side of diagonal elements
		System.out.print (" Diagonal one : ");
		for (int i = 0; i < row; i++)
		{
	
			// printing direct square of diagonal
			// element there is no need to check
			// condition
			System.out.print( mat[i][i] * mat[i][i] +" ");
		}
		System.out.println();
	
		// This loop is for finding square of the
		// second side of diagonal elements
		System.out.print( " Diagonal two : ");
		for (int i = 0; i < row; i++)
		{
			// printing direct square of diagonal
			// element in the second side
			System.out.print( mat[i][row - i - 1] *
							mat[i][row - i - 1] + " ");
		}
	}
	
	// Driver code
	public static void main (String[] args)
	{
		int mat[][] = { { 2, 5, 7 },
						{ 3, 7, 2 },
						{ 5, 6, 9 } };
		diagonalsquare(mat, 3, 3);
	
	}
}

// This code is contributed by vt_m.
