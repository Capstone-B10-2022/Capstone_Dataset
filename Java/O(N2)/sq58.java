// Simple JAva program to print squares of
// diagonal elements.
//https://www.geeksforgeeks.org/squares-of-matrix-diagonal-elements/
import java.io.*;

class sq58
{
	static int MAX =100;
	
	// function of diagonal square
	static void diagonalsquare(int mat[][], int row,
										int column)
	{
		// This loop is for finding square of first
		// diagonal elements
		System.out.print( "Diagonal one : ");
		for (int i = 0; i < row; i++)
		{
			for (int j = 0; j < column; j++)
	
				// if this condition will become true
				// then we will get diagonal element
				if (i == j)
	
					// printing square of diagonal element
					System.out.print ( mat[i][j] * mat[i][j] +" ");
		}
		System.out.println();
	
		// This loop is for finding square of second
		// side of diagonal elements
		System.out.print("Diagonal two : ");
		for (int i = 0; i < row; i++)
		{
			for (int j = 0; j < column; j++)
	
				// if this condition will become true
				// then we will get second side diagonal
				// element
				if (i + j == column - 1)
	
					// printing square of diagonal element
					System.out.print(mat[i][j] * mat[i][j] +" ");
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
