// Source: https://www.geeksforgeeks.org/c-program-multiply-two-matrices/

/*
* This Java program can multiply any two square or
* rectangular matrices. The below program multiplies two
* square matrices of size 4 * 4. There is also an example
* of a rectangular matrix for the same code (commented
* below). We can change the Matrix value with the number of
* rows and columns for Matrix-1 and Matrix-2
* for different dimensions.
*/

/*
* Note: i- The number of columns in Matrix-1 must be equal
* to the number of rows in Matrix-2. ii- Output of
* multiplication of Matrix-1 and Matrix-2, results with
* equal to the number of rows of Matrix-1 and the number of
* columns of Matrix-2 i.e. rslt[R1][C2].
*/

import java.io.*;
import java.util.*;

class ON3_10 {
	
	static int R1 = 4; // number of rows in Matrix-1
	static int C1 = 4; // number of columns in Matrix-1
	static int R2 = 4; // number of rows in Matrix-2
	static int C2 = 4; // number of columns in Matrix-2
	
	// This function multiplies mat1[][]
	// and mat2[][], and stores the result
	// in res[][]
	static void mulMat(int[][] mat1, int[][] mat2)
	{
		// To store result
		int[][] rslt = new int[R1][C2];
		System.out.println("Multiplication of given two matrices is:");
		int i, j, k;
		for (i = 0; i < R1; i++) {
			for (j = 0; j < C2; j++) {
				rslt[i][j] = 0;
				for (k = 0; k < R2; k++)
					rslt[i][j] += mat1[i][k] * mat2[k][j];
				System.out.print(rslt[i][j] + " ");
			}
			System.out.println("");
		}
	}
	
	// Driver program
	public static void main (String[] args) {
		int[][] mat1 = { { 1, 1, 1, 1 },
						{ 2, 2, 2, 2 },
						{ 3, 3, 3, 3 },
						{ 4, 4, 4, 4 } };

		int[][] mat2 = { { 1, 1, 1, 1 },
						{ 2, 2, 2, 2 },
						{ 3, 3, 3, 3 },
						{ 4, 4, 4, 4 } };
						
		/*
		// Rectangular Matrices
		// R1 = 3, C1 = 4 and R2 = 4, C2 = 3 (Update these values in the global variables)
		int mat1[][] = {
						{1, 1, 1, 1},
						{2, 2, 2, 2},
						{3, 3, 3, 3} };
	
		int mat2[][] = {
						{1, 1, 1},
						{2, 2, 2},
						{3, 3, 3},
						{4, 4, 4} };
		*/

		if (C1 != R2) {
			System.out.println("The number of columns in Matrix-1 must be equal to the number of rows in Matrix-2");
			System.out.println("Please update the global variables according to your array dimension");
		}
		else {
			mulMat(mat1, mat2);
		}
	}
}
//This code is contributed by shruti456rawal
