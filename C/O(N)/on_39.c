// Source: https://www.geeksforgeeks.org/given-an-array-a-and-a-number-x-check-for-pair-in-a-with-sum-as-x/

// C program to check if given array
// has 2 elements whose sum is equal
// to the given value

#include <stdio.h>
#define MAX 100000

// NOTE: Works only if range elements is limited
// target - arr[i] >= 0 && target - arr[i] < MAX



void printPairs(int arr[], int arr_size, int target)
{
	int i, temp;

	/*initialize hash set as 0*/
	int s[MAX] = { 0 };

	for (i = 0; i < arr_size; i++)
	{
		temp = target - arr[i];
		if (s[temp] == 1)
			printf(
				"Pair with given sum %d is (%d, %d) \n",
				target, arr[i], temp);
		s[arr[i]] = 1;
	}
}

/* Driver Code */
int main()
{
	int A[] = { 1, 4, 45, 6, 10, 8 };
	int target = 16;
	int arr_size = sizeof(A) / sizeof(A[0]);

	printPairs(A, arr_size, target);

	getchar();
	return 0;
}
