// Source: https://www.geeksforgeeks.org/check-rows-matrix-circular-rotations/

// Java program to check if all rows of a matrix
// are rotations of each other
class ON3_7
{

	static int MAX = 1000;

	// Returns true if all rows of mat[0..n-1][0..n-1]
	// are rotations of each other.
	static boolean isPermutedMatrix(int mat[][], int n)
	{
		// Creating a string that contains
		// elements of first row.
		String str_cat = "";
		for (int i = 0; i < n; i++)
		{
			str_cat = str_cat + "-" + String.valueOf(mat[0][i]);
		}

		// Concatenating the string with itself
		// so that substring search operations
		// can be performed on this
		str_cat = str_cat + str_cat;

		// Start traversing remaining rows
		for (int i = 1; i < n; i++)
		{
			// Store the matrix into vector in the form
			// of strings
			String curr_str = "";
			for (int j = 0; j < n; j++)
			{
				curr_str = curr_str + "-" + String.valueOf(mat[i][j]);
			}

			// Check if the current string is present in
			// the concatenated string or not
			if (str_cat.contentEquals(curr_str))
			{
				return false;
			}
		}

		return true;
	}

	// Drivers code
	public static void main(String[] args)
	{
		int n = 4;
		int mat[][] = {{1, 2, 3, 4},
		{4, 1, 2, 3},
		{3, 4, 1, 2},
		{2, 3, 4, 1}
		};
		if (isPermutedMatrix(mat, n))
		{
			System.out.println("Yes");
		}
		else
		{
			System.out.println("No");
		}
	}
}

/* This code contributed by PrinciRaj1992 */
