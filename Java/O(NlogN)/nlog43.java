// Java program to print all distinct
// elements in a given array
//https://www.geeksforgeeks.org/print-distinct-elements-given-integer-array/
import java.io.*;
import java .util.*;

class nlog43
{
	static void printDistinct(int arr[], int n)
	{
		// First sort the array so that
		// all occurrences become consecutive
		Arrays.sort(arr);
	
		// Traverse the sorted array
		for (int i = 0; i < n; i++)
		{
			// Move the index ahead while
			// there are duplicates
			while (i < n - 1 && arr[i] == arr[i + 1])
				i++;
	
			// print last occurrence of
			// the current element
			System.out.print(arr[i] +" ");
		}
	}
	
	// Driver program
	public static void main (String[] args)
	{
		int arr[] = {6, 10, 5, 4, 9, 120, 4, 6, 10};
		int n = arr.length;
		printDistinct(arr, n);

	}
}

// This code is contributed by vt_m
