// Source: https://www.geeksforgeeks.org/queries-for-decimal-values-of-subarray-of-a-binary-array/

// Java implementation of finding number
// represented by binary subarray
import java.util.Arrays;

class ON_87 {

	// Fills pre[]
	static void precompute(int arr[], int n, int pre[])
	{
		Arrays.fill(pre, 0);

		pre[n - 1] = arr[n - 1] * (int)(Math.pow(2, 0));
		for (int i = n - 2; i >= 0; i--)
			pre[i] = pre[i + 1] + arr[i] * (1 << (n - 1 - i));
	}

	// returns the number represented by a binary
	// subarray l to r
	static int decimalOfSubarr(int arr[], int l, int r,
							int n, int pre[])
	{

		// if r is equal to n-1 r+1 does not exist
		if (r != n - 1)
			return (pre[l] - pre[r + 1]) / (1 << (n - 1 - r));

		return pre[l] / (1 << (n - 1 - r));
	}

	// Driver code
	public static void main(String[] args)
	{
		int arr[] = { 1, 0, 1, 0, 1, 1 };
		int n = arr.length;

		int pre[] = new int[n];
		precompute(arr, n, pre);

		System.out.println(decimalOfSubarr(arr,
										2, 4, n, pre));

		System.out.println(decimalOfSubarr(arr,
										4, 5, n, pre));
	}
}

// This code is contributed by Anant Agarwal.

