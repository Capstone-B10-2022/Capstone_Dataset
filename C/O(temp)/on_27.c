// Source: https://www.geeksforgeeks.org/maximum-sum-such-that-no-two-elements-are-adjacent/

// C code to implement the approach
 
#include <stdio.h>
 
// Function to return max sum such that
// no two elements are adjacent
int findMaxSum(int arr[], int n)
{
    int incl = arr[0];
    int excl = 0;
    int excl_new;
    int i;
 
    for (i = 1; i < n; i++) {
         
        // Current max excluding i
        excl_new = (incl > excl) ? incl : excl;
 
        // Current max including i
        incl = excl + arr[i];
        excl = excl_new;
    }
 
    // Return max of incl and excl
    return ((incl > excl) ? incl : excl);
}
 
// Driver code
int main()
{
    int arr[] = { 5, 5, 10, 100, 10, 5 };
    int N = sizeof(arr) / sizeof(arr[0]);
     
    // Function call
    printf("%d", findMaxSum(arr, N));
    return 0;
}