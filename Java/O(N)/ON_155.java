// Source: https://www.geeksforgeeks.org/a-product-array-puzzle/


class ON_155 {
	void productArray(int arr[], int n)
	{

		// Base case
		if (n == 1) {
			System.out.print("0");
			return;
		}

		int i, temp = 1;

		/* Allocate memory for the product array */
		int prod[] = new int[n];

		/* Initialize the product array as 1 */
		for (int j = 0; j < n; j++)
			prod[j] = 1;

		/* In this loop, temp variable contains product of
		elements on left side excluding arr[i] */
		for (i = 0; i < n; i++) {
			prod[i] = temp;
			temp *= arr[i];
		}

		/* Initialize temp to 1 for product on right side */
		temp = 1;

		/* In this loop, temp variable contains product of
		elements on right side excluding arr[i] */
		for (i = n - 1; i >= 0; i--) {
			prod[i] *= temp;
			temp *= arr[i];
		}

		/* print the constructed prod array */
		for (i = 0; i < n; i++)
			System.out.print(prod[i] + " ");

		return;
	}

	/* Driver program to test above functions */
	public static void main(String[] args)
	{
		ON_155 pa = new ON_155();
		int arr[] = { 10, 3, 5, 6, 2 };
		int n = arr.length;
		System.out.println("The product array is : ");
		pa.productArray(arr, n);
	}
}

// This code has been contributed by Mayank Jaiswal

