// Source: https://www.geeksforgeeks.org/find-repetitive-element-1-n-1/

// Java program to find the only
// repeating element in an array
// where elements are from 1 to N-1.
import java.lang.Math.*;

class ON_129 {

	// Function to find repeated element
	static int findRepeating(int arr[], int N)
	{
		int missingElement = 0;

		// indexing based
		for (int i = 0; i < N; i++) {

			int absVal = Math.abs(arr[i]);
			int element = arr[absVal];

			if (element < 0) {
				missingElement = arr[i];
				break;
			}

			absVal = Math.abs(arr[i]);
			arr[absVal] = -arr[absVal];
		}

		return Math.abs(missingElement);
	}

	// Driver code
	public static void main(String[] args)
	{
		int arr[] = { 9, 8, 2, 6, 1, 8, 5, 3, 4, 7 };

		int N = arr.length;
	
		// Function call
		System.out.println(findRepeating(arr, N));
	}
}
// This code is contributed by
// Smitha Dinesh Semwal.
