// Source: https://www.geeksforgeeks.org/search-insert-and-delete-in-a-sorted-array/

// Java program to insert an
// element in a sorted array

class ON_122 {
	// Inserts a key in arr[] of given
	// capacity. n is current size of arr[].
	// This function returns n+1 if insertion
	// is successful, else n.
	static int insertSorted(int arr[], int n, int key, int capacity)
	{
		// Cannot insert more elements if n is already
		// more than or equal to capacity
		if (n >= capacity)
			return n;

		int i;
		for (i = n - 1; (i >= 0 && arr[i] > key); i--)
			arr[i + 1] = arr[i];

		arr[i + 1] = key;

		return (n + 1);
	}

	/* Driver program to test above function */
	public static void main(String[] args)
	{
		int arr[] = new int[20];
		arr[0] = 12;
		arr[1] = 16;
		arr[2] = 20;
		arr[3] = 40;
		arr[4] = 50;
		arr[5] = 70;
		int capacity = arr.length;
		int n = 6;
		int key = 26;

		System.out.print("\nBefore Insertion: ");
		for (int i = 0; i < n; i++)
			System.out.print(arr[i] + " ");

		// Inserting key
		n = insertSorted(arr, n, key, capacity);

		System.out.print("\nAfter Insertion: ");
		for (int i = 0; i < n; i++)
			System.out.print(arr[i] + " ");
	}
}
