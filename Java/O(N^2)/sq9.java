// A O(n) time and O(1) extra space Java program to
// sort an array according to given indexes

class sq9 {
	public static void swap(int arr[], int a, int b)
	{
		int temp = arr[a];
		arr[a] = arr[b];
		arr[b] = temp;
	}
	// Function to reorder elements of arr[] according
	// to index[]
	public static void reorder(int arr[], int index_arr[],
							int n)
	{
		// Fix all elements one by one
		for (int i = 0; i < n; i++) {
			// While index[i] and arr[i] are not fixed
			while (index_arr[i] != i) {
				swap(arr, i, index_arr[i]);
				swap(index_arr, i, index_arr[i]);
			}
		}
	}
	// Driver program
	public static void main(String[] args)
	{
		int arr[] = { 50, 40, 70, 60, 90 };
		int index[] = { 3, 0, 4, 1, 2 };
		int n = arr.length;
		reorder(arr, index, n);
		System.out.print("Reordered array is: \n");
		for (int i = 0; i < n; i++) {
			System.out.print(arr[i] + " ");
		}
		System.out.print("\nModified Index array is: \n");
		for (int i = 0; i < n; i++) {
			System.out.print(index[i] + " ");
		}
	}
}

// This code is contributed by Tapesh(tapeshdua420)
