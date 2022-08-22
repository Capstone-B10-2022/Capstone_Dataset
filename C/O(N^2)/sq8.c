// C program for above approach
#include <stdio.h>

// Function to transform the array
void fixArray(int ar[], int n)
{
	int i, j, temp;

	// Iterate over the array
	for (i = 0; i < n; i++)
	{
		for (j = 0; j < n; j++)
		{
			// Check is any ar[j]
			// exists such that
			// ar[j] is equal to i
			if (ar[j] == i) {
				temp = ar[j];
				ar[j] = ar[i];
				ar[i] = temp;
				break;
			}
		}
	}

	// Iterate over array
	for (i = 0; i < n; i++)
	{
		// If not present
		if (ar[i] != i)
		{
			ar[i] = -1;
		}
	}

	// Print the output
	printf("Array after Rearranging\n");
	for (i = 0; i < n; i++) {
		printf("%d ",ar[i]);
	}
}

// Driver Code
int main()
{
	int n, ar[] = { -1, -1, 6, 1, 9, 3, 2, -1, 4, -1 };
	n = sizeof(ar) / sizeof(ar[0]);

	// Function Call
	fixArray(ar, n);
}

// This code is contributed by kothvvsaakash.
