// Source: https://www.geeksforgeeks.org/given-an-array-a-and-a-number-x-check-for-pair-in-a-with-sum-as-x/

// Java implementation using Hashing
import java.io.*;
import java.util.HashSet;

class ON_124 {
	static void printpairs(int arr[], int sum)
	{
		HashSet<Integer> s = new HashSet<Integer>();
		for (int i = 0; i < arr.length; ++i)
		{
			int temp = sum - arr[i];

			// checking for condition
			if (s.contains(temp)) {
				System.out.println(
					"Pair with given sum "
					+ sum + " is (" + arr[i]
					+ ", " + temp + ")");
			}
			s.add(arr[i]);
		}
	}

	// Driver Code
	public static void main(String[] args)
	{
		int A[] = { 1, 4, 45, 6, 10, 8 };
		int n = 16;
		printpairs(A, n);
	}
}

// This article is contributed by Aakash Hasija

