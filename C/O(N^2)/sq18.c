// C code to find Two elements
// whose sum is closest to zero
//https://www.geeksforgeeks.org/two-elements-whose-sum-is-closest-to-zero/
# include <stdio.h>
# include <stdlib.h> /* for abs() */
# include <math.h>
void minAbsSumPair(int arr[], int arr_size)
{
int inv_count = 0;
int l, r, min_sum, sum, min_l, min_r;

/* Array should have at least two elements*/
if(arr_size < 2)
{
	printf("Invalid Input");
	return;
}

/* Initialization of values */
min_l = 0;
min_r = 1;
min_sum = arr[0] + arr[1];

for(l = 0; l < arr_size - 1; l++)
{
	for(r = l+1; r < arr_size; r++)
	{
	sum = arr[l] + arr[r];
	if(abs(min_sum) > abs(sum))
	{
		min_sum = sum;
		min_l = l;
		min_r = r;
	}
	}
}

printf(" The two elements whose sum is minimum are %d and %d",
		arr[min_l], arr[min_r]);
}

/* Driver program to test above function */
int main()
{
int arr[] = {1, 60, -10, 70, -80, 85};
minAbsSumPair(arr, 6);
getchar();
return 0;
}
