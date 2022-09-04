// Source: geeksforgeeks.org/find-the-two-repeating-elements-in-a-given-array/


// Java program to Find the two repeating
// elements in a given array
import java.util.*;
class ON_149{

static void printRepeating(int arr[], int size)
{
	HashSet<Integer>s = new HashSet<>();
	System.out.print("The two Repeating elements are : ");
	for(int i = 0; i < size; i++)
	{
	if(!s.isEmpty() && s.contains(arr[i]))
		System.out.print(arr[i]+" ");
	s.add(arr[i]);
	}
}

// Driver code
public static void main(String[] args)
{
	int arr[] = {4, 2, 4, 5, 2, 3, 1};
	int arr_size = arr.length;
	printRepeating(arr, arr_size);
}
}

// This code is contributed by Rajput-Ji

