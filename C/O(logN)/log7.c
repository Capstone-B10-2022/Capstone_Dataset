// C program to find the smallest elements missing
// in a sorted array.
//https://www.geeksforgeeks.org/find-the-first-missing-number/
#include<stdio.h>

int findFirstMissing(int array[], int start, int end)
{
	if (start > end)
		return end + 1;

	if (start != array[start])
		return start;

	int mid = (start + end) / 2;

	// Left half has all elements from 0 to mid
	if (array[mid] == mid)
		return findFirstMissing(array, mid+1, end);

	return findFirstMissing(array, start, mid);
}

// driver program to test above function
int main()
{
	int arr[] = {0, 1, 2, 3, 4, 5, 6, 7, 10};
	int n = sizeof(arr)/sizeof(arr[0]);
	printf("Smallest missing element is %d",
		findFirstMissing(arr, 0, n-1));
	return 0;
}
