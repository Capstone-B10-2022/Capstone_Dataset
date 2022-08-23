// Java program to perform range queries over range
// queries.
// https://www.geeksforgeeks.org/array-range-queries-range-queries/
public class log1 {

	static final int max = 10000;

// For prefix sum array
	static void update(int arr[], int l) {
		arr[l] += arr[l - 1];
	}

// This function is used to apply square root
// decomposition in the record array
	static void record_func(int block_size, int block[],
			int record[], int l, int r, int value) {
		// traversing first block in range
		while (l < r && l % block_size != 0 && l != 0) {
			record[l] += value;
			l++;
		}
		// traversing completely overlapped blocks in range
		while (l + block_size <= r + 1) {
			block[l / block_size] += value;
			l += block_size;
		}
		// traversing last block in range
		while (l <= r) {
			record[l] += value;
			l++;
		}
	}
// Function to print the resultant array

	static void print(int arr[], int n) {
		for (int i = 0; i < n; i++) {
			System.out.print(arr[i] + " ");
		}
	}

// Driver code
	public static void main(String[] args) {

		int n = 5, m = 5;
		int arr[] = new int[n], record[] = new int[m];
		int block_size = (int) Math.sqrt(m);
		int block[] = new int[max];
		int command[][] = {{1, 1, 2}, {1, 4, 5},
		{2, 1, 2}, {2, 1, 3},
		{2, 3, 4}};

		for (int i = m - 1; i >= 0; i--) {

			// If query is of type 2 then function
			// call to record_func
			if (command[i][0] == 2) {
				int x = i / (block_size);
				record_func(block_size, block, record,
						command[i][1] - 1, command[i][2] - 1,
						(block[x] + record[i] + 1));
			} // If query is of type 1 then simply add
			// 1 to the record array
			else {
				record[i]++;
			}
		}

		// Merging the value of the block in the record array
		for (int i = 0; i < m; i++) {
			int check = (i / block_size);
			record[i] += block[check];
		}

		for (int i = 0; i < m; i++) {
			// If query is of type 1 then the array
			// elements are over-written by the record
			// array
			if (command[i][0] == 1) {
				arr[command[i][1] - 1] += record[i];
				if ((command[i][2] - 1) < n - 1) {
					arr[(command[i][2])] -= record[i];
				}
			}
		}

		// The prefix sum of the array
		for (int i = 1; i < n; i++) {
			update(arr, i);
		}

		// Printing the resultant array
		print(arr, n);

	}

}
// This code is contributed by 29AjayKumar
