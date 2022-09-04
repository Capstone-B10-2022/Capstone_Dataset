// Source: https://www.geeksforgeeks.org/maximum-equilibrium-sum-in-an-array/

// Java program to find maximum equilibrium
// sum.
import java.lang.Math.*;
import java.util.stream.*;

class ON_131 {
	
	// Function to find maximum equilibrium
	// sum.
	static int findMaxSum(int arr[], int n)
	{
		int sum = IntStream.of(arr).sum();
		int prefix_sum = 0,
		res = Integer.MIN_VALUE;
		
		for (int i = 0; i < n; i++)
		{
			prefix_sum += arr[i];
			
			if (prefix_sum == sum)
				res = Math.max(res, prefix_sum);
			sum -= arr[i];
		}
		
		return res;
	}
	
	// Driver Code
	public static void main(String[] args)
	{
		int arr[] = { -2, 5, 3, 1,
					2, 6, -4, 2 };
		int n = arr.length;
		System.out.print(findMaxSum(arr, n));
	}
}

// This code is contributed by Smitha.

