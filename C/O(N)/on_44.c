// Source: https://www.geeksforgeeks.org/check-for-majority-element-in-a-sorted-array/

/* C Program to check for majority element in a sorted array */
# include <stdio.h>
# include <stdbool.h>

bool isMajority(int arr[], int n, int x)
{
	int i;

	/* get last index according to n (even or odd) */
	int last_index = n%2? (n/2+1): (n/2);

	/* search for first occurrence of x in arr[]*/
	for (i = 0; i < last_index; i++)
	{
		/* check if x is present and is present more than n/2
		times */
		if (arr[i] == x && arr[i+n/2] == x)
			return 1;
	}
	return 0;
}

/* Driver program to check above function */
int main()
{
	int arr[] ={1, 2, 3, 4, 4, 4, 4};
	int n = sizeof(arr)/sizeof(arr[0]);
	int x = 4;
	if (isMajority(arr, n, x))
		printf("%d appears more than %d times in arr[]",
			x, n/2);
	else
		printf("%d does not appear more than %d times in arr[]",
				x, n/2);

return 0;
}
