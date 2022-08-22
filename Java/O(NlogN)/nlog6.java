// Java program for the above approach

import java.util.*;

class nlog6 {
	static int Kth_smallest(TreeMap<Integer, Integer> mp,
							int K)
	{
		int freq = 0;
		for (Map.Entry it : mp.entrySet()) {

			// adding the frequencies of each element
			freq += (int)it.getValue();

			// if at any point frequency becomes
			// greater than or equal to k then
			// return that element
			if (freq >= K) {
				return (int)it.getKey();
			}
		}

		return -1; // returning -1 if k>size of the array
				// which is an impossible scenario
	}

	// Driver's code
	public static void main(String[] args)
	{
		int N = 5;
		int K = 2;
		int[] arr = { 12, 3, 5, 7, 19 };
		TreeMap<Integer, Integer> mp = new TreeMap<>();

		for (int i = 0; i < N; i++) {

			// mapping every element with
			// it's
			// frequency
			mp.put(arr[i], mp.getOrDefault(arr[i], 0) + 1);
		}

		// Function call
		int ans = Kth_smallest(mp, K);

		System.out.println(
			"The " + K + "th smallest element is " + ans);
	}
}

// This code is contributed by harshit17.
