////geeksforgeeks.org/find-a-peak-in-a-given-array/
// A Java program to find a peak element using divide and
// conquer

//The below-given code is the iterative version of the above explained and demonstrated recursive based divide and conquer technique.
import java.io.*;

class log21 {

	// A binary search based function that returns index of
	// a peak element
	static int findPeak(int arr[], int n)
	{
		int l = 0;
		int r = n-1;
		int mid = 0;
	
		while (l <= r) {

			// finding mid by binary right shifting.
			mid = (l + r) >> 1;

			// first case if mid is the answer
			if ((mid == 0
				|| arr[mid - 1] <= arr[mid])
						&& (mid == n - 1
							|| arr[mid + 1] <= arr[mid]))
				break;

			// move the right pointer
			if (mid > 0 && arr[mid - 1] > arr[mid])
				r = mid - 1;

			// move the left pointer
			else
				l = mid + 1;
		}
	
		return mid;
	}

	// Driver Code
	public static void main(String args[])
	{
		int arr[] = { 1, 3, 20, 4, 1, 0 };
		int n = arr.length;
		System.out.println("Index of a peak point is "
						+ findPeak(arr, n));
	}
}

// This code is contributed by Rajdeep Mallick (rajdeep999)
