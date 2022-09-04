// Source: https://www.geeksforgeeks.org/a-product-array-puzzle/


// C implementation of above approach
#include <stdio.h>
#include <string.h>
// Function to print product array for a given array arr[]
// of size n
void productArray(int arr[], int n)
{

	// Base case
	if (n == 1) {
		printf("0");
		return;
	}

	int i, temp = 1;

	/* Allocate memory for the product array */
	int prod[n];

	/* Initialize the product array as 1 */
	memset(prod, 1, n);

	/* In this loop, temp variable contains product of
	elements on left side excluding arr[i] */
	for (i = 0; i < n; i++) {
		prod[i] = temp;
		temp *= arr[i];
	}

	/* Initialize temp to 1
	for product on right side */
	temp = 1;

	/* In this loop, temp variable contains product of
	elements on right side excluding arr[i] */
	for (i = n - 1; i >= 0; i--) {
		prod[i] *= temp;
		temp *= arr[i];
	}

	/* print the constructed prod array */
	for (i = 0; i < n; i++)
		printf("%d ", prod[i]);

	return;
}

// Driver Code
int main()
{
	int arr[] = { 10, 3, 5, 6, 2 };
	int n = sizeof(arr) / sizeof(arr[0]);
	printf("The product array is: \n");
	productArray(arr, n);
}

// This code is contributed by Aditya Kumar (adityakumar129)
