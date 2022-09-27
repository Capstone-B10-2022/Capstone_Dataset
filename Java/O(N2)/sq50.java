// Java program to rotate a
// matrix by 90 degrees
//https://www.geeksforgeeks.org/inplace-rotate-square-matrix-by-90-degrees/
import java.io.*;

class sq50 {

// Function to reverse
// the given 2D arr[][]
static void Reverse(int i,int mat[][], int N)
{
	// Initialise start and end index
	int start = 0;
	int end = N - 1;

	// Till start < end, swap the element
	// at start and end index
	while (start < end) {

	// Swap the element
	int temp = mat[i][start];
	mat[i][start] = mat[i][end];
	mat[i][end] = temp;

	// Increment start and decrement
	// end for next pair of swapping
	start++;
	end--;
	}
}

// An Inplace function to
// rotate a N x N matrix
// by 90 degrees in
// anti-clockwise direction

static void rotateMatrix(int N, int mat[][])
{ // REVERSE every row
	for (int i = 0; i < N; i++)
	Reverse(i,mat,N);

	// Performing Transpose
	for (int i = 0; i < N; i++) {
	for (int j = i; j < N; j++)
	{
		int temp=mat[i][j];
		mat[i][j]=mat[j][i];
		mat[j][i]=temp;
	}
	}
}

// Function to print the matrix
static void displayMatrix(int N, int mat[][])
{
	for (int i = 0; i < N; i++) {
	for (int j = 0; j < N; j++)
		System.out.print(" " + mat[i][j]);

	System.out.print("\n");
	}
	System.out.print("\n");
}

/* Driver program to test above functions */
public static void main(String[] args)
{
	int N = 4;

	// Test Case 1
	int mat[][] = { { 1, 2, 3, 4 },
				{ 5, 6, 7, 8 },
				{ 9, 10, 11, 12 },
				{ 13, 14, 15, 16 } };

	rotateMatrix(N, mat);

	// Print rotated matrix
	displayMatrix(N, mat);
}
}

// This code is contributed by Aarti_Rathi
