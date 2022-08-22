// Java program to find K
// maximum combinations
// from two arrays,
import java.io.*;
import java.util.*;

class sq17 {

	// function to display first K
	// maximum sum combinations
	static void KMaxCombinations(int A[], int B[],
								int N, int K)
	{
		// max heap.
		PriorityQueue<Integer> pq
			= new PriorityQueue<Integer>(
				Collections.reverseOrder());

		// Insert all the possible
		// combinations in max heap.
		for (int i = 0; i < N; i++)
			for (int j = 0; j < N; j++)
				pq.add(A[i] + B[j]);

		// Pop first N elements
		// from max heap and
		// display them.
		int count = 0;

		while (count < K) {
			System.out.println(pq.peek());
			pq.remove();
			count++;
		}
	}

	// Driver Code
	public static void main(String[] args)
	{
		int A[] = { 4, 2, 5, 1 };
		int B[] = { 8, 0, 5, 3 };
		int N = A.length;
		int K = 3;

		// Function Call
		KMaxCombinations(A, B, N, K);
	}
}

// This code is contributed by Mayank Tyagi
