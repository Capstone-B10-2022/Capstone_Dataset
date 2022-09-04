// Source: https://www.geeksforgeeks.org/sort-1-n-swapping-adjacent-elements/

// Java program to test whether an array
// can be sorted by swapping adjacent
// elements using boolean array
class ON_109
{
	// Return true if array can be
	// sorted otherwise false
	static int sortedAfterSwap(int[] A,
							int[] B, int n)
	{
		int t = 0;
		for (int i = 0; i < n - 1; i++)
		{
			if (B[i] != 0)
			{
				if (A[i] != i + 1)
					t = A[i];
					A[i] = A[i + 1];
					A[i + 1] = t;
			}
		}
	
		// Check if array is sorted or not
		for (int i = 0; i < n; i++)
		{
			if (A[i] != i + 1)
				return 0;
		}
	
		return 1;
	}
	
	// Driver Code
	public static void main(String[] args)
	{
		int[] A = { 1, 2, 5, 3, 4, 6 };
		int[] B = { 0, 1, 1, 1, 0 };
		int n = A.length;
	
		if (sortedAfterSwap(A, B, n) == 0)
			System.out.println("A can be sorted");
		else
			System.out.println("A can not be sorted");
	}
}

// This code is contributed
// by Mukul Singh.

