// Source: https://www.geeksforgeeks.org/move-zeroes-end-array/

// C Program to move all zeros to the end
#include <stdio.h>
int main()
{
    int A[] = { 5, 6, 0, 4, 6, 0, 9, 0, 8 };
    int n = sizeof(A) / sizeof(A[0]);
    int j = 0;
    for (int i = 0; i < n; i++) {
        if (A[i] != 0) {
            int temp = A[i]; // Partitioning the array
            A[i] = A[j];
            A[j] = temp;
            j++;
        }
    }
    for (int i = 0; i < n; i++) {
        printf("%d ", A[i]); // Print the array
    }
 
    return 0;
}