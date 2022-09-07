// Java program to find the only repeating
// element in an array where elements are
// from 1 to N-1.
//https://www.geeksforgeeks.org/find-repetitive-element-1-n-1/
import java.util.Arrays;

public class nlog45 {
	static int findRepeating(int[] arr, int N)
	{
		Arrays.sort(arr); // sort array
	
		for (int i = 0; i < N; i++) {
		
			// compare array element with its index
			if (arr[i] != i + 1) {
				return arr[i];
			}
		}
		return -1;
	}

	// Driver's code
	static public void main(String[] args)
	{
		int[] arr
			= new int[] { 9, 8, 2, 6, 1, 8, 5, 3, 4, 7 };
		int N = arr.length;
	
		// Function call
		int repeatingNum = findRepeating(arr, N);
		System.out.println(repeatingNum);
	}
}

// This code is contributed by Abhijeet Kumar(abhijeet19403)
