// Java Program for above approach
//https://www.geeksforgeeks.org/find-the-first-missing-number/
import java.io.*;

class log9
{

	// Program to find Smallest
	// Missing in Sorted Array
	int findSmallestMissinginSortedArray(
							int[] arr)
	{
	// Check if 0 is missing
	// in the array
	if(arr[0] != 0)
		return 0;
	
	// Check is all numbers 0 to n - 1
	// are present in array
	if(arr[arr.length-1] == arr.length - 1)
		return arr.length;
	
	int first = arr[0];

	return findFirstMissing(arr,0,
					arr.length-1,first);
	}
	
	// Program to find missing element
	int findFirstMissing(int[] arr , int start ,
							int end, int first)
	{
	
	if (start < end)
	{
		int mid = (start+end)/2;

		/** Index matches with value
		at that index, means missing
		element cannot be upto that point */
		if (arr[mid] != mid+first)
		return findFirstMissing(arr, start,
									mid , first);
		else
		return findFirstMissing(arr, mid+1,
									end , first);
	}
	return start+first;

	}

	// Driver program to test the above function
	public static void main(String[] args)
	{
		GFG small = new GFG();
		int arr[] = {0, 1, 2, 3, 4, 5, 7};
		int n = arr.length;
		
		// Function Call
		System.out.println("First Missing element is : "
			+ small.findSmallestMissinginSortedArray(arr));
	}
}
