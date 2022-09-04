// Source: https://www.geeksforgeeks.org/check-if-array-elements-are-consecutive/

//Code is contributed by Dhananjay Dhawale @chessnoobdj

#include<stdio.h>
#include<stdlib.h>

/* UTILITY FUNCTIONS */
int getMin(int arr[], int n)
{
	int min = arr[0];
	for (int i = 1; i < n; i++)
		if (arr[i] < min)
			min = arr[i];
	return min;
}
int areConsecutive(int arr[], int n)
{
	int min_ele = getMin(arr, n), num = 0;
	for(int i=0; i<n; i++){
		num ^= min_ele^arr[i];
		min_ele += 1;
	}
	if(num == 0)
		return 1;
	return 0;
}

/* Driver program to test above functions */
int main()
{
	int arr[]= {1, 4, 5, 3, 2, 6};
	int n = sizeof(arr)/sizeof(arr[0]);
	if(areConsecutive(arr, n) == 1)
		printf(" Array elements are consecutive ");
	else
		printf(" Array elements are not consecutive ");
	getchar();
	return 0;
}
