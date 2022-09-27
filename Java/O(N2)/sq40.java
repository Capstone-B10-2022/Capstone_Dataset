// Java program to find the only repeating
// element in an array where elements are
// from 1 to N-1.using System;
//https://www.geeksforgeeks.org/find-repetitive-element-1-n-1/
public class sq40 {
	static int findRepeating(int[] arr)
	{
		for (int i = 0; i < arr.length; i++) {
			for (int j = i + 1; j < arr.length; j++) {
				if (arr[i] == arr[j])
					return arr[i];
			}
		}
		return -1;
	}

	// Driver's code
	static public void main(String[] args)
	{

		// Code
		int[] arr
			= new int[] { 9, 8, 2, 6, 1, 8, 5, 3, 4, 7 };
		int repeatingNum = findRepeating(arr);

		// Function call
		System.out.println(repeatingNum);
	}
}

// This code is contributed by phasing17
