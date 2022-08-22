// C code to find largest three elements in an array
#include <stdio.h>
#include <stdlib.h>

// Compare function for qsort
int cmpfunc(const void* a, const void* b)
{
	return (*(int*)a - *(int*)b);
}

void find3largest(int arr[], int n)
{
	qsort(arr, n, sizeof(int),
		cmpfunc); // It uses Tuned Quicksort with
	// avg. case Time complexity = O(nLogn)

	int check = 0, count = 1;
	for (int i = 1; i <= n; i++) {
		if (count < 4) {
			if (check != arr[n - i]) {
				// to handle duplicate values
				printf("%d ", arr[n - i]);
				check = arr[n - i];
				count++;
			}
		}
		else
			break;
	}
}

// Driver code
int main()
{
	int arr[] = { 12, 45, 1, -1, 45, 54, 23, 5, 0, -10 };
	int n = sizeof(arr) / sizeof(arr[0]);
	find3largest(arr, n);
}

// This code is contributed by Aditya Kumar (adityakumar129)
