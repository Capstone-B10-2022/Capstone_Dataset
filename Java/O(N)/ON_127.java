// Source: https://www.geeksforgeeks.org/find-repetitive-element-1-n-1/

// Java program to find the only repeating
// element in an array where elements are
// from 1 to N-1.
import java.io.*;
import java.util.*;

class ON_127 {

	static int findRepeating(int[] arr, int N)
	{
		// Find array sum and subtract sum
		// first n-1 natural numbers from it
		// to find the result.

		int sum = 0;
		for (int i = 0; i < N; i++)
			sum += arr[i];
		return sum - (((N - 1) * N) / 2);
	}

	// Driver's code
	public static void main(String args[])
	{
		int[] arr = { 9, 8, 2, 6, 1, 8, 5, 3, 4, 7 };
		int N = arr.length;
		
		// Function call
		System.out.println(findRepeating(arr, N));
	}
}

// This code is contributed by rachana soma

