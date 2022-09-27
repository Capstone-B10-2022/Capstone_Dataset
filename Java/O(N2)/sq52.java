// Java program to find
// the scalar product
// of a matrix
//https://www.geeksforgeeks.org/program-for-scalar-multiplication-of-a-matrix/
import java.io.*;

class sq52 {
	
static final int N = 3;
static void scalarProductMat(int mat[][],
								int k)
{
	
	// scalar element is multiplied
	// by the matrix
	for (int i = 0; i < N; i++)
		for (int j = 0; j < N; j++)
			mat[i][j] = mat[i][j] * k;
}

// Driver code
public static void main (String[] args)
{
	int mat[][] = { { 1, 2, 3 },
					{ 4, 5, 6 },
					{ 7, 8, 9 } };
	int k = 4;

	scalarProductMat(mat, k);

	// to display the resultant matrix
	System.out.println("Scalar Product Matrix is : ");
	
	for (int i = 0; i < N; i++)
	{
		for (int j = 0; j < N; j++)
			System.out.print(mat[i][j] + " ");
		System.out.println();
	}
}
}

// This code is contributed by Ajit.
