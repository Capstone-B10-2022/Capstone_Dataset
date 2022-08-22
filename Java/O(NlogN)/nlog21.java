// Java program to find mean
// and median of an array
import java.util.*;

class nlog21
{

	// Function for calculating median
	public static double findMedian(int a[], int n)
	{
		// First we sort the array
		Arrays.sort(a);

		// check for even case
		if (n % 2 != 0)
			return (double)a[n / 2];

		return (double)(a[(n - 1) / 2] + a[n / 2]) / 2.0;
	}

	// Driver code
	public static void main(String args[])
	{
		int a[] = { 1, 3, 4, 2, 7, 5, 8, 6 };
		int n = a.length;
	
		// Function call
		
		System.out.println("Median = " + findMedian(a, n));
	}
}

// This article is contributed by Anshika Goyal.
