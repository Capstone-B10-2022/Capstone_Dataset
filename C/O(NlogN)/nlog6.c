
// C program to rearrange the elements in array such that
// even positioned are greater than odd positioned elements
#include <stdio.h>
#include <stdlib.h>
 
// Compare function for qsort
int cmpfunc(const void* a, const void* b)
{
    return (*(int*)a - *(int*)b);
}
 
void assign(int a[], int n)
{
    // Sort the array
    qsort(a, n, sizeof(int), cmpfunc);
 
    int ans[n];
    int p = 0, q = n - 1;
    for (int i = 0; i < n; i++) {
        // Assign even indexes with maximum elements
        if ((i + 1) % 2 == 0)
            ans[i] = a[q--];
        // Assign odd indexes with remaining elements
        else
            ans[i] = a[p++];
    }
 
    // Print result
    for (int i = 0; i < n; i++)
        printf("%d ", ans[i]);
}
 
// Driver Code
int main()
{
    int A[] = { 1, 3, 2, 2, 5 };
    int n = sizeof(A) / sizeof(A[0]);
    assign(A, n);
    return 0;
}
 
// This code is contributed by Sania Kumari Gupta