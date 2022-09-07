// Java implementation using STL
//https://www.geeksforgeeks.org/two-elements-whose-sum-is-closest-to-zero/
import java.io.*;

class nlog36{
	
static void findMinSum(int[] arr, int n)
{
	for(int i = 1; i < n; i++)
	{
		if (!(Math.abs(arr[i - 1]) <
			Math.abs(arr[i])))
		{
			int temp = arr[i - 1];
			arr[i - 1] = arr[i];
			arr[i] = temp;
		}
	}
	int min = Integer.MAX_VALUE;
	int x = 0, y = 0;
	
	for(int i = 1; i < n; i++)
	{
		
		// Absolute value shows how close
		// it is to zero
		if (Math.abs(arr[i - 1] + arr[i]) <= min)
		{
			
			// If found an even close value
			// update min and store the index
			min = Math.abs(arr[i - 1] + arr[i]);
			x = i - 1;
			y = i;
		}
	}
	System.out.println("The two elements whose " +
					"sum is minimum are " +
					arr[x] + " and " + arr[y]);
}

// Driver code
public static void main(String[] args)
{
	int[] arr = { 1, 60, -10, 70, -80, 85 };
	int n = arr.length;
	
	findMinSum(arr, n);
}
}

// This code is contributed by rag2127
