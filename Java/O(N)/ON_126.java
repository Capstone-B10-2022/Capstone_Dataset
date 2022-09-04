// Source: https://www.geeksforgeeks.org/find-repetitive-element-1-n-1/

import java.util.*;
// Java program to find the only repeating
// element in an array where elements are
// from 1 to N-1.

class ON_126 {

	static int findRepeating(int arr[], int N)
	{
		HashSet<Integer> s = new HashSet<Integer>();
		for (int i = 0; i < N; i++) {
			if (s.contains(arr[i]))
				return arr[i];
			s.add(arr[i]);
		}

		// If input is correct, we should
		// never reach here
		return -1;
	}

	// Driver's code
	public static void main(String[] args)
	{
		int arr[] = { 9, 8, 2, 6, 1, 8, 5, 3, 4, 7 };
		int N = arr.length;
	
		// Function call
		System.out.println(findRepeating(arr, N));
	}
}

// This code is contributed by Rajput-Ji

