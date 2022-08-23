// C program to find maximum sum of all
// rotation of i*arr[i] using pivot.
#include<stdio.h>
 
// fun declaration
int maxSum(int arr[], int n);
int findPivot(int arr[], int n);
 
// function definition
int maxSum(int arr[], int n)
{
    int sum = 0;
    int i;
    int pivot = findPivot(arr, n);
 
    // difference in pivot and index of
    // last element of array
    int diff = n - 1 - pivot;
    for(i = 0; i < n; i++)
    {
        sum= sum + ((i + diff) % n) * arr[i];
    }
    return sum;
}
 
// function to find pivot
int findPivot(int arr[], int n)
{
    int i;
    for(i = 0; i < n; i++)
    {
        if(arr[i] > arr[(i + 1) % n])
            return i;
    }
}
 
// Driver code
int main(void)
{
     
    // rotated input array
    int arr[] = {8, 3, 1, 2};
    int n = sizeof(arr) / sizeof(int);
    int max = maxSum(arr, n);
    printf("%d", max);
    return 0;
}