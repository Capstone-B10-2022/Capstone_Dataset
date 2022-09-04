// Source: https://www.geeksforgeeks.org/c-program-multiply-two-matrices/

// Java program to multiply two matrices.

public class ON3_8
{

	/**
	* to find out matrix multiplication
	*
	* @param matrix1 First matrix
	* @param rows1 Number of rows in matrix 1
	* @param cols1 Number of columns in matrix 1
	* @param matrix2 Second matrix
	* @param rows2 Number of rows in matrix 2
	* @param cols2 Number of columns in matrix 2
	* @return the result matrix (matrix 1 and matrix 2
	* multiplication)
	*/
	public static int[][] matrixMultiplication(
		int[][] matrix1, int rows1, int cols1,
		int[][] matrix2, int rows2, int cols2)
		throws Exception
	{

		// Required condition for matrix multiplication
		if (cols1 != rows2) {
			throw new Exception("Invalid matrix given.");
		}

		// create a result matrix
		int resultMatrix[][] = new int[rows1][cols2];

		// Core logic for 2 matrices multiplication
		for (int i = 0; i < resultMatrix.length; i++)
		{
			for (int j = 0;
				j < resultMatrix[i].length;
				j++)
			{
				for (int k = 0; k < cols1; k++)
				{
					resultMatrix[i][j]
						+= matrix1[i][k] * matrix2[k][j];
				}
			}
		}
		return resultMatrix;
	}

	// Driver code
	public static void main(String[] args) throws Exception
	{

		// Initial matrix 1 and matrix 2
		int matrix1[][] = { { 2, 4 }, { 3, 4 } };
		int matrix2[][] = { { 1, 2 }, { 1, 3 } };

		// Function call to get a matrix multiplication
		int resultMatrix[][] = matrixMultiplication(
			matrix1, 2, 2, matrix2, 2, 2);

		// Display result matrix
		System.out.println("Result Matrix is:");
		for (int i = 0; i < resultMatrix.length; i++)
		{
			for (int j = 0;
				j < resultMatrix[i].length;
				j++)
			{
				System.out.print(resultMatrix[i][j] + "\t");
			}
			System.out.println();
		}
	}
	// This code is contributed by darshatandel1998 (Darshan
	// Tandel)
}

