// Java program to find Majority
// element in an array
//https://www.geeksforgeeks.org/majority-element/
import java.io.*;
import java.util.*;

class nlog46{

// Function to find Majority element
// in an array it returns -1 if there
// is no majority element
public static int majorityElement(int[] arr, int n)
{
	
	// Sort the array in O(nlogn)
	Arrays.sort(arr);

	int count = 1, max_ele = -1,
		temp = arr[0], ele = 0,
			f = 0;

	for(int i = 1; i <= n; i++)
	{
		
		// Increases the count if the
		// same element occurs otherwise
		// starts counting new element
		if (temp == arr[i])
		{
			count++;
		}
		else
		{
			count = 1;
			temp = arr[i];
		}

		// Sets maximum count and stores
		// maximum occurred element so far
		// if maximum count becomes greater
		// than n/2 it breaks out setting
		// the flag
		if (max_ele < count)
		{
			max_ele = count;
			ele = arr[i];

			if (max_ele > (n / 2))
			{
				f = 1;
				break;
			}
		}
	}

	// Returns maximum occurred element
	// if there is no such element, returns -1
	return (f == 1 ? ele : -1);
}

// Driver code
public static void main(String[] args)
{
	int arr[] = { 1, 1, 2, 1, 3, 5, 1 };
	int n = 7;

	System.out.println(majorityElement(arr, n));
}
}

// This code is contributed by RohitOberoi
