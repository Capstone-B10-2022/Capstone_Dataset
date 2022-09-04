// Source: https://www.geeksforgeeks.org/find-element-appears-array-every-element-appears-twice/

// Java program to find the array
// element that appears only once
class ON_130
{
	// Return the maximum Sum of difference
	// between consecutive elements.
	static int findSingle(int ar[], int ar_size)
	{
		// Do XOR of all elements and return
		int res = ar[0];
		for (int i = 1; i < ar_size; i++)
			res = res ^ ar[i];
	
		return res;
	}

	// Driver code
	public static void main (String[] args)
	{
		int ar[] = {2, 3, 5, 4, 5, 3, 4};
		int n = ar.length;
		System.out.println("Element occurring once is " +
							findSingle(ar, n) + " ");
	}
}
// This code is contributed by Prakriti Gupta

