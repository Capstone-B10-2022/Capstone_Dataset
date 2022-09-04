// Source: https://www.geeksforgeeks.org/a-product-array-puzzle/

// C program for the above approach
#include <stdio.h>

void productExceptSelf(int a[], int n)
{
	long prod = 1;
	long flag = 0;

	// product of all elements
	for (int i = 0; i < n; i++) {
		// counting number of elements which have value 0
		if (a[i] == 0)
			flag++;
		else
			prod *= a[i];
	}

	// creating a new array of size n
	long arr[n];

	for (int i = 0; i < n; i++) {

		// if number of elements in array with value 0 is
		// more than 1 than each value in new array will be
		// equal to 0
		if (flag > 1)
			arr[i] = 0;

		// if no element having value 0 than we will insert
		// product/a[i] in new array
		else if (flag == 0)
			arr[i] = (prod / a[i]);

		// if 1 element of array having value 0 than all the
		// elements except that index value , will be equal
		// to 0
		else if (flag == 1 && a[i] != 0)
			arr[i] = 0;

		// if(flag == 1 && a[i] == 0)
		else
			arr[i] = prod;
	}
	for (int i = 0; i < n; i++)
		printf("%ld ", arr[i]);
}

// Driver Code
int main()
{
	int n = 5;
	int array[] = { 10, 3, 5, 6, 2 };
	productExceptSelf(array, n);
	return 0;
}

// This code is contributed by Aditya Kumar (adityakumar129)
