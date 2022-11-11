//https://www.geeksforgeeks.org/count-1s-sorted-binary-array/
/*package whatever //do not write package name here */
import java.io.*;

class log21 {

	static int countOnes(int arr[], int n)
	{
		int ans;
		int low = 0, high = n - 1;
		while (low <= high) { // get the middle index
			int mid = (low + high) / 2;

			// else recur for left side
			if (arr[mid] < 1)
				high = mid - 1;

			// If element is not last 1, recur for right
			// side
			else if (arr[mid] > 1)
				low = mid + 1;
			else

			// check if the element at middle index is last
			// 1
			{
				if (mid == n - 1 || arr[mid + 1] != 1)
					return mid + 1;
				else
					low = mid + 1;
			}
		}
		return 0;
	}

	// Driver code
	public static void main(String[] args)
	{

		int arr[] = { 1, 1, 1, 1, 0, 0, 0 };
		int n = arr.length;

		System.out.println("Count of 1's in given array is "
						+ countOnes(arr, n));
	}
}

// This code is contributed by patel2127.
