// C program to rearrange the array as per the given
// condition
#include <stdio.h>
#include <stdlib.h>

// Compare function for qsort
int cmpfunc(const void* a, const void* b)
{
	return (*(int*)a - *(int*)b);
}

// function to rearrange the array
void rearrangeArr(int arr[], int n)
{
	// total even positions
	int evenPos = n / 2;
	// total odd positions
	int oddPos = n - evenPos;
	int tempArr[n];

	// copy original array in an auxiliary array
	for (int i = 0; i < n; i++)
		tempArr[i] = arr[i];

	// sort the auxiliary array
	qsort(tempArr, n, sizeof(int), cmpfunc);
	int j = oddPos - 1;

	// fill up odd position in original array
	for (int i = 0; i < n; i += 2)
		arr[i] = tempArr[j--];

	j = oddPos;

	// fill up even positions in original array
	for (int i = 1; i < n; i += 2)
		arr[i] = tempArr[j++];

	// display array
	for (int i = 0; i < n; i++)
		printf("%d ", arr[i]);
}

// Driver code
int main()
{
	int arr[] = { 1, 2, 3, 4, 5, 6, 7 };
	int size = sizeof(arr) / sizeof(arr[0]);
	rearrangeArr(arr, size);
	return 0;
}

// This code is contributed by Sania Kumari Gupta
