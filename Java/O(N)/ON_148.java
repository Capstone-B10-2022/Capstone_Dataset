// Source: geeksforgeeks.org/find-the-two-repeating-elements-in-a-given-array/

import java.io.*;

class ON_148 {

	public static void twoRepeated(int arr[], int N)
	{
		int m = N - 1;
		for (int i = 0; i < N; i++) {
			arr[arr[i] % m - 1] += m;

			if ((arr[arr[i] % m - 1] / m) == 2)
				System.out.printf(arr[i] % m + " ");
		}
	}

	// Driver code
	public static void main(String[] args)
	{
		int arr[] = { 4, 2, 4, 5, 2, 3, 1 };
		int n = 7;
		System.out.printf(
			"The two repeating elements are ");
		twoRepeated(arr, n);
	}
}

// This code is contributed by Aditya Kumar (adityakumar129)

