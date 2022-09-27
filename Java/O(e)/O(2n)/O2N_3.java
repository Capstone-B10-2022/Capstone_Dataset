// Source: https://www.geeksforgeeks.org/array-range-queries-range-queries/

// Java program to perform range queries
// over range queries.
import java.util.*;

class O2N_3
{

	// Function to execute type 1 query
	static void type1(int[] arr, int start, int limit)
	{

		// incrementing the array by 1 for type
		// 1 queries
		for (int i = start; i <= limit; i++)
			arr[i]++;
	}

	// Function to execute type 2 query
	static void type2(int[] arr, int[][] query,
					int start, int limit)
	{
		for (int i = start; i <= limit; i++)
		{

			// If the query is of type 1 function
			// call to type 1 query
			if (query[i][0] == 1)
				type1(arr, query[i][1], query[i][2]);

			// If the query is of type 2 recursive call
			// to type 2 query
			else if (query[i][0] == 2)
				type2(arr, query, query[i][1],
								query[i][2]);
		}
	}

	// Driver Code
	public static void main(String[] args)
	{

		// Input size of array and number of queries
		int n = 5, m = 5;
		int[] arr = new int[n + 1];

		// Build query matrix
		int[] temp = { 1, 1, 2, 1, 4, 5, 2,
					1, 2, 2, 1, 3, 2, 3, 4 };
		int[][] query = new int[6][4];
		int j = 0;
		for (int i = 1; i <= m; i++)
		{
			query[i][0] = temp[j++];
			query[i][1] = temp[j++];
			query[i][2] = temp[j++];
		}

		// Perform queries
		for (int i = 1; i <= m; i++)
			if (query[i][0] == 1)
				type1(arr, query[i][1], query[i][2]);
			else if (query[i][0] == 2)
				type2(arr, query, query[i][1],
								query[i][2]);

		// printing the result
		for (int i = 1; i <= n; i++)
			System.out.print(arr[i] + " ");
		System.out.println();
	}
}

// This code is contributed by
// sanjeev2552

