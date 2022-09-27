// Java program to perform range queries
// over range queries.
//https://www.geeksforgeeks.org/array-range-queries-range-queries/
import java.util.Arrays;

class sq20
{

	// Function to create the record array
	static void record_sum(int record[], int l,
						int r, int n, int adder)
	{
		for (int i = l; i <= r; i++)
		{
			record[i] += adder;
		}
	}

	// Driver Code
	public static void main(String[] args)
	{
		int n = 5, m = 5;
		int arr[] = new int[n];

		// Build query matrix
		Arrays.fill(arr, 0);
		int query[][] = {{1, 1, 2}, {1, 4, 5},
						{2, 1, 2}, {2, 1, 3},
						{2, 3, 4}};
		int record[] = new int[m];
		Arrays.fill(record, 0);

		for (int i = m - 1; i >= 0; i--)
		{

			// If query is of type 2 then function
			// call to record_sum
			if (query[i][0] == 2)
			{
				record_sum(record, query[i][1] - 1,
								query[i][2] - 1, m,
								record[i] + 1);
			}
			
			// If query is of type 1 then
			// simply add 1 to the record array
			else
			{
				record_sum(record, i, i, m, 1);
			}

		}

		// for type 1 queries adding the contains of
		// record array to the main array record array
		for (int i = 0; i < m; i++)
		{
			if (query[i][0] == 1)
			{
				record_sum(arr, query[i][1] - 1,
								query[i][2] - 1,
								n, record[i]);
			}
		}

		// printing the array
		for (int i = 0; i < n; i++)
		{
			System.out.print(arr[i] + " ");
		}
	}
}

// This code is contributed
// by Princi Singh
