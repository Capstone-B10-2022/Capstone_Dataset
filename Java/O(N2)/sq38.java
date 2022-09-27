// Java program to print all distinct
// elements in a given array
//https://www.geeksforgeeks.org/print-distinct-elements-given-integer-array/
import java.io.*;

class GFG {

	static void printDistinct(int arr[], int n)
	{
		// Pick all elements one by one
		for (int i = 0; i < n; i++)
		{
			// Check if the picked element
			// is already printed
			int j;
			for (j = 0; j < i; j++)
			if (arr[i] == arr[j])
				break;
	
			// If not printed earlier,
			// then print it
			if (i == j)
			System.out.print( arr[i] + " ");
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
