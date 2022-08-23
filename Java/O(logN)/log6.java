/*package whatever //do not write package name here */
import java.io.*;
//https://www.geeksforgeeks.org/find-rotation-count-rotated-sorted-array/
class log6{
	// Returns count of rotations
	// for an array which is first sorted
	// in ascending order, then rotated

	// Observation: We have to return
	// index of the smallest element
	static int countRotations(int[] arr, int n)
	{
		int low = 0, high = n - 1;
		while (low <= high) {

			// if first element is mid or
			// last element is mid
			// then simply use modulo so it
			// never goes out of bound.
			int mid = low + (high - low) / 2;
			int prev = (mid - 1 + n) % n;
			int next = (mid + 1) % n;

			if (arr[mid] <= arr[prev]
				&& arr[mid] <= arr[next])
				return mid;
			else if (arr[mid] <= arr[high])
				high = mid - 1;
			else if (arr[mid] >= arr[low])
				low = mid + 1;
		}
		return 0;
	}

	// Driver Code
	public static void main(String args[])
	{

		int[] arr = { 15, 18, 2, 3, 6, 12 };
		int n = arr.length;
		System.out.println(countRotations(arr, n));
	}
}

// This code is contributed by shinjanpatra
