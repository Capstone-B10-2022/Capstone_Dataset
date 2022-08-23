// Efficient C++ program to count number
// of elements with values in given range.
//https://www.geeksforgeeks.org/queries-counts-array-elements-values-given-range/
import java.io.*;
import java.util.Arrays;

class nlog32
{
	// function to find first index >= x
	static int lowerIndex(int arr[], int n, int x)
	{
		int l = 0, h = n - 1;
		while (l <= h)
		{
			int mid = (l + h) / 2;
			if (arr[mid] >= x)
				h = mid - 1;
			else
				l = mid + 1;
		}
		return l;
	}
	
	// function to find last index <= y
	static int upperIndex(int arr[], int n, int y)
	{
		int l = 0, h = n - 1;
		while (l <= h)
		{
			int mid = (l + h) / 2;
			if (arr[mid] <= y)
				l = mid + 1;
			else
				h = mid - 1;
		}
		return h;
	}
	
	// function to count elements within given range
	static int countInRange(int arr[], int n, int x, int y)
	{
		// initialize result
		int count = 0;
		count = upperIndex(arr, n, y) -
				lowerIndex(arr, n, x) + 1;
		return count;
	}
	
	// Driver function
	public static void main (String[] args)
	{
		int arr[] = { 1, 4, 4, 9, 10, 3 };
		int n = arr.length;
	
		// Preprocess array
		Arrays.sort(arr);
	
		// Answer queries
		int i = 1, j = 4;
		System.out.println( countInRange(arr, n, i, j)); ;
	
		i = 9;
		j = 12;
		System.out.println( countInRange(arr, n, i, j));
	

	}
}

// This article is contributed by vt_m.
