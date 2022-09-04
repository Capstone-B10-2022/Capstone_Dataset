// Source: https://www.geeksforgeeks.org/count-pairs-difference-equal-k/

/* An efficient program to count pairs with difference k when the range
numbers is small */

static int MAX = 100000;
public static int ON_115(int arr[], int n, int k)
{
	int count = 0; // Initialize count

	// Initialize empty hashmap.
	boolean hashmap[MAX] = {false};

	// Insert array elements to hashmap
	for (int i = 0; i < n; i++)
		hashmap[arr[i]] = true;

	for (int i = 0; i < n; i++)
	{
		int x = arr[i];
		if (x - k >= 0 && hashmap[x - k])
			count++;
		if (x + k < MAX && hashmap[x + k])
			count++;
		hashmap[x] = false;
	}
	return count;
}

// This code is contributed by RohitOberoi.

