/*
* This C program tells if there exists a pair in array whose sum results in x.
*/
//https://www.geeksforgeeks.org/given-an-array-a-and-a-number-x-check-for-pair-in-a-with-sum-as-x/
#include <stdio.h>

// Function to find and print pair
int chkPair(int A[], int size, int x) {
	for (int i = 0; i < (size - 1); i++) {
		for (int j = (i + 1); j < size; j++) {
			if (A[i] + A[j] == x) {
				printf("Pair with a given sum %d is (%d, %d)\n", x, A[i], A[j]);

				return 1;
			}
		}
	}

	return 0;
}

int main(void) {
	int A[] = {0, -1, 2, -3, 1};
	int x = -2;
	int size = sizeof(A) / sizeof(A[0]);

	if (chkPair(A, size, x)) {
		printf("Valid pair exists\n");
	}
	else {
		printf("No valid pair exists for %d\n", x);
	}

	return 0;
}
// This code is contributed by Manish Kumar (mkumar2789)
