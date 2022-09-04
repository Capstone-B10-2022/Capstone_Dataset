// Source; https://www.geeksforgeeks.org/find-the-two-repeating-elements-in-a-given-array/

#include <stdio.h>
#include <stdlib.h>

void printRepeating(int arr[], int size)
{
int i;

printf("\n The repeating elements are");
	
for(i = 0; i < size; i++)
{
	if(arr[abs(arr[i])] > 0)
	arr[abs(arr[i])] = -arr[abs(arr[i])];
	else
	printf(" %d ", abs(arr[i]));
}		
}	

int main()
{
int arr[] = {4, 2, 4, 5, 2, 3, 1};
int arr_size = sizeof(arr)/sizeof(arr[0]);
printRepeating(arr, arr_size);
getchar();
return 0;
}
