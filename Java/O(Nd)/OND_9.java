// Source: https://www.geeksforgeeks.org/find-subarray-least-average/

// java program code of Naive approach to
// find subarray with minimum average
import java.util.*;

class OND_9 {

	static void findsubarrayleast(int arr[], int k, int n)
	{
		int min = Integer.MAX_VALUE;
		int minindex = 0;
		for (int i = 0; i <= n - k; i++) {
			int sum = 0;
			for (int j = i; j < i + k; j++) {
				sum += arr[j];
			}
			if (sum < min) {
				min = sum;
				minindex = i;
			}
		}
		// printing the desired subarray
		System.out.println(
			"subarray with minimum average is: ");
		for (int i = minindex; i < minindex + k; i++) {
			System.out.print(arr[i] + " ");
		}
	}

	// Driver Code
	public static void main(String[] args)
	{
		// Test Case 1
		int arr[] = {20, 3, 13, 5, 10, 14, 8, 5, 11, 9, 1, 11};
		int n = arr.length;
		int k = 9;

		// function call
		findsubarrayleast(arr, k, n);
	}
}

// This code is contributed by Aarti_Rathi

