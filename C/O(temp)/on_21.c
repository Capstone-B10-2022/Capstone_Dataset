// Source: https://www.geeksforgeeks.org/rearrange-array-arrj-becomes-arri-j/

// A simple C program to rearrange contents of arr[]
// such that arr[j] becomes j if arr[i] is j
#include <stdio.h>
 
// A simple method to rearrange 'arr[0..n-1]' so that 'arr[j]'
// becomes 'i' if 'arr[i]' is 'j'
void rearrangeNaive(int arr[], int n)
{
    // Create an auxiliary array of same size
    int temp[n], i;
 
    // Store result in temp[]
    for (i = 0; i < n; i++)
        temp[arr[i]] = i;
 
    // Copy temp back to arr[]
    for (i = 0; i < n; i++)
        arr[i] = temp[i];
}
 
// A utility function to print contents of arr[0..n-1]
void printArray(int arr[], int n)
{
    int i;
    for (i = 0; i < n; i++)
        printf("%d ", arr[i]);
    printf("\n");
}
 
// Driver program
int main()
{
    int arr[] = { 1, 3, 0, 2 };
    int n = sizeof(arr) / sizeof(arr[0]);
 
    printf("Given array is \n");
    printArray(arr, n);
 
    rearrangeNaive(arr, n);
 
    printf("Modified array is \n");
    printArray(arr, n);
    return 0;
}