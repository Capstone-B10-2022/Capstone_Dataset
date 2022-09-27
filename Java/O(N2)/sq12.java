// Java program to rearrange positive
// and negative numbers
import java.io.*;
import java.util.*;

class sq12
{

	// Swap function
	static void swap(int[] a, int i, int j)
	{
		int temp = a[i];
		a[i] = a[j];
		a[j] = temp;
	}

	// Print array function
	static void printArray(int[] a, int n)
	{
		for (int i = 0; i < n; i++)
			System.out.print(a[i] + " ");
		System.out.println();
	}

	// Driver code
	public static void main(String args[])
	{
		int[] arr = { 1, -3, 5, 6, -3, 6, 7, -4, 9, 10 };
		int n = arr.length;
			
		//before modification
		printArray(arr, n);

		for (int i = 0; i < n; i++)
		{
			if (arr[i] >= 0 && i % 2 == 1)
			{
				// out of order positive element
				for (int j = i + 1; j < n; j++)
				{
					if (arr[j] < 0 && j % 2 == 0)
					{
						// find out of order negative
						// element in remaining array
						swap(arr, i, j);
						break ;
					}
				}
			}

			else if (arr[i] < 0 && i % 2 == 0)
			{
				// out of order negative element
				for (int j = i + 1; j < n; j++)
				{
					if (arr[j] >= 0 && j % 2 == 1)
					{
						// find out of order positive
						// element in remaining array
						swap(arr, i, j);
						break;
					}
				}
			}
		}

		//after modification
		printArray(arr, n);
	}
}

// This code is contributed by rachana soma
