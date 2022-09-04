// Source: https://www.geeksforgeeks.org/print-distinct-elements-given-integer-array/

/* Java program to print all distinct elements of a given array */
import java.util.*;

class ON_116
{
	// This function prints all distinct elements
	static void printDistinct(int arr[])
	{
		// Creates an empty hashset
		HashSet<Integer> set = new HashSet<>();

		// Traverse the input array
		for (int i=0; i<arr.length; i++)
		{
			// If not present, then put it in hashtable and print it
			if (!set.contains(arr[i]))
			{
				set.add(arr[i]);
				System.out.print(arr[i] + " ");
			}
		}
	}

	// Driver method to test above method
	public static void main (String[] args)
	{
		int arr[] = {10, 5, 3, 4, 3, 5, 6};
		printDistinct(arr);
	}
}

