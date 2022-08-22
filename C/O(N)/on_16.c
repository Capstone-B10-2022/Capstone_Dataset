// Source: https://www.geeksforgeeks.org/rearrange-positive-and-negative-numbers-publish/

// A C++ program to put positive numbers at even indexes (0,
// 2, 4,..) and negative numbers at odd indexes (1, 3, 5, ..)
#include <stdio.h>
 
// prototype for swap
void swap(int *a, int *b);
 
// The main function that rearranges elements of given array.
// It puts  positive elements at even indexes (0, 2, ..) and
// negative numbers at odd indexes (1, 3, ..).
void rearrange(int arr[], int n)
{
    // The following few lines are similar to partition process
    // of QuickSort.  The idea is to consider 0 as pivot and
    // divide the array around it.
    int i = -1;
    for (int j = 0; j < n; j++)
    {
        if (arr[j] < 0)
        {
            i++;
            swap(&arr[i], &arr[j]);
        }
    }
 
    // Now all positive numbers are at end and negative numbers
    // at the beginning of array. Initialize indexes for starting
    // point of positive and negative numbers to be swapped
    int pos = i+1, neg = 0;
 
    // Increment the negative index by 2 and positive index by 1,
    // i.e., swap every alternate negative number with next
    // positive number
    while (pos < n && neg < pos && arr[neg] < 0)
    {
        swap(&arr[neg], &arr[pos]);
        pos++;
        neg += 2;
    }
}
 
// A utility function to swap two elements
void swap(int *a, int *b)
{
    int temp = *a;
    *a = *b;
    *b = temp;
}
 
// A utility function to print an array
void printArray(int arr[], int n)
{
    for (int i = 0; i < n; i++)
        printf("%4d ", arr[i]);
}
 
// Driver program to test above functions
int main()
{
    int arr[] = {-1, 2, -3, 4, 5, 6, -7, 8, 9};
    int n = sizeof(arr)/sizeof(arr[0]);
    rearrange(arr, n);
    printArray(arr, n);
    return 0;
}