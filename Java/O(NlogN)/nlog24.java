// Java program to find k-th absolute difference
// between two elements
import java.util.Scanner;
import java.util.Arrays;

class nlog24
{
	// returns number of pairs with absolute
	// difference less than or equal to mid
	static int countPairs(int[] a, int n, int mid)
	{
		int res = 0, value;
		for(int i = 0; i < n; i++)
		{
			// Upper bound returns pointer to position
			// of next higher number than a[i]+mid in
			// a[i..n-1]. We subtract (ub + i + 1) from
			// this position to count
			if(a[i]+mid>a[n-1])
			res+=(n-(i+1));
			else
			{
			int ub = upperbound(a, n, a[i]+mid);
			res += (ub- (i+1));
			}
		}
		return res;
	}

	// returns the upper bound
	static int upperbound(int a[], int n, int value)
	{
		int low = 0;
		int high = n;
		while(low < high)
		{
			final int mid = (low + high)/2;
			if(value >= a[mid])
				low = mid + 1;
			else
				high = mid;
		}

	return low;
	}

	// Returns k-th absolute difference
	static int kthDiff(int a[], int n, int k)
	{
		// Sort array
		Arrays.sort(a);

		// Minimum absolute difference
		int low = a[1] - a[0];
		for (int i = 1; i <= n-2; ++i)
			low = Math.min(low, a[i+1] - a[i]);

		// Maximum absolute difference
		int high = a[n-1] - a[0];

		// Do binary search for k-th absolute difference
		while (low < high)
		{
			int mid = (low + high) >> 1;
			if (countPairs(a, n, mid) < k)
				low = mid + 1;
			else
				high = mid;
		}

		return low;
	}

	// Driver function to check the above functions
	public static void main(String args[])
	{
		Scanner s = new Scanner(System.in);
		int k = 3;
		int a[] = {1,2,3,4};
		int n = a.length;
		System.out.println(kthDiff(a, n, k));
	}

}
// This code is contributed by nishkarsh146
