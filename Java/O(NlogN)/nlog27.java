/*package whatever //do not write package name here */

import java.io.*;
import java.util.*;

class nlog27 {
//Java simple approach to print smallest
//and second smallest element.

// Driver Code
public static void main(String args[])
{
	int arr[]={111, 13, 25, 9, 34, 1};
	int n=arr.length;

	// sorting the array using
	// in-built sort function
	Arrays.sort(arr);

	// printing the desired element
	System.out.println("smallest element is "+arr[0]);
	System.out.println("second smallest element is "+arr[1]);
}
}

// This code is contributed by shinjanpatra
