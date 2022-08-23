// Java program for the above approach
//https://www.geeksforgeeks.org/java-program-to-generate-a-matrix-having-sum-of-secondary-diagonal-equal-to-a-perfect-square/
class sq24 {

	// Function to print the matrix whose sum
	// of element in secondary diagonal is a
	// perfect square
	static void diagonalSumPerfectSquare(int[] arr,
										int N)
	{

		// Iterate for next N - 1 rows
		for (int i = 0; i < N; i++)
		{

			// Print the current row after
			// the left shift
			for (int j = 0; j < N; j++)
			{
				System.out.print(arr[(j + i) % 7] + " ");
			}
			System.out.println();
		}
	}

	// Driver Code
	public static void main(String[] srgs)
	{

		// Given N
		int N = 7;

		int[] arr = new int[N];

		// Fill the array with elements
		// ranging from 1 to N
		for (int i = 0; i < N; i++)
		{
			arr[i] = i + 1;
		}

		// Function Call
		diagonalSumPerfectSquare(arr, N);
	}
}

// This code is contributed by Amit Katiyar
