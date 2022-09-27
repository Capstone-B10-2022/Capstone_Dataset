// Java for printing smallest k numbers in order
import java.lang.*;
import java.util.*;

public class sq18 {
	// Function to print smallest k numbers
	// in arr[0..n-1]
	public static void printSmall(int arr[], int n, int k)
	{
		// For each arr[i] find whether
		// it is a part of n-smallest
		// with insertion sort concept
		for (int i = k; i < n; ++i) {
			// Find largest from top n-element
			int max_var = arr[k - 1];
			int pos = k - 1;
			for (int j = k - 2; j >= 0; j--) {
				if (arr[j] > max_var) {
					max_var = arr[j];
					pos = j;
				}
			}

			// If largest is greater than arr[i]
			// shift all element one place left
			if (max_var > arr[i]) {
				int j = pos;
				while (j < k - 1) {
					arr[j] = arr[j + 1];
					j++;
				}
				// make arr[k-1] = arr[i]
				arr[k - 1] = arr[i];
			}
		}
		// print result
		for (int i = 0; i < k; i++)
			System.out.print(arr[i] + " ");
	}

	// Driver function
	public static void main(String argc[])
	{
		int[] arr = { 1, 5, 8, 9, 6, 7, 3, 4, 2, 0 };
		int n = 10;
		int k = 5;
		printSmall(arr, n, k);
	}
}
