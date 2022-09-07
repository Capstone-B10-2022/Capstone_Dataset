/* A simple program to print
subarray with sum as given sum */
//https://www.geeksforgeeks.org/find-subarray-with-given-sum/
#include <stdio.h>

/* Returns true if the there is a subarray
of arr[] with a sum equal to 'sum'
otherwise returns false. Also, prints
the result */
int subArraySum(int arr[], int n, int sum)
{
	int currentSum, i, j;

	// Pick a starting point
	for (i = 0; i < n; i++) {
		currentSum = arr[i];

		// try all subarrays starting with 'i'
		for (j = i + 1; j <= n; j++) {
			if (currentSum == sum) {
				printf(
					"Sum found between indexes %d and %d",
					i, j - 1);
				return 1;
			}
			if (currentSum > sum || j == n)
				break;
			currentSum = currentSum + arr[j];
		}
	}

	printf("No subarray found");
	return 0;
}

// Driver program to test above function
int main()
{
	int arr[] = { 15, 2, 4, 8, 9, 5, 10, 23 };
	int n = sizeof(arr) / sizeof(arr[0]);
	int sum = 23;
	subArraySum(arr, n, sum);
	return 0;
}
