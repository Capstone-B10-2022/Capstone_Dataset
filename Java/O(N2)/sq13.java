// Java code for kth smallest element in an array

import java.util.Arrays;
import java.util.Collections;

class sq13 {
	// Standard partition process of QuickSort.
	// It considers the last element as pivot
	// and moves all smaller element to left of
	// it and greater elements to right
	public static int partition(Integer[] arr, int l, int r)
	{
		int x = arr[r], i = l;
		for (int j = l; j <= r - 1; j++) {
			if (arr[j] <= x) {

				// Swapping arr[i] and arr[j]
				int temp = arr[i];
				arr[i] = arr[j];
				arr[j] = temp;

				i++;
			}
		}

		// Swapping arr[i] and arr[r]
		int temp = arr[i];
		arr[i] = arr[r];
		arr[r] = temp;

		return i;
	}

	// This function returns k'th smallest element
	// in arr[l..r] using QuickSort based method.
	// ASSUMPTION: ALL ELEMENTS IN ARR[] ARE DISTINCT
	public static int kthSmallest(Integer[] arr, int l,
								int r, int K)
	{
		// If k is smaller than number of elements
		// in array
		if (K > 0 && K <= r - l + 1) {

			// Partition the array around last
			// element and get position of pivot
			// element in sorted array
			int pos = partition(arr, l, r);

			// If position is same as k
			if (pos - l == K - 1)
				return arr[pos];

			// If position is more, recur for
			// left subarray
			if (pos - l > K - 1)
				return kthSmallest(arr, l, pos - 1, K);

			// Else recur for right subarray
			return kthSmallest(arr, pos + 1, r,
							K - pos + l - 1);
		}

		// If k is more than number of elements
		// in array
		return Integer.MAX_VALUE;
	}

	// Driver's code
	public static void main(String[] args)
	{
		Integer arr[]
			= new Integer[] { 12, 3, 5, 7, 4, 19, 26 };
		int K = 3;

		// Function call
		System.out.print(
			"K'th smallest element is "
			+ kthSmallest(arr, 0, arr.length - 1, K));
	}
}

// This code is contributed by Chhavi
