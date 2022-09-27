// C program for rearrange an
// array such that arr[i] = i.
#include <stdio.h>

// Function to rearrange an array
// such that arr[i] = i.
void fixArray(int A[], int len)
{
	for (int i = 0; i < len; i++)
	{
		if (A[i] != -1 && A[i] != i)
		{
			int x = A[i];

			// check if desired place
			// is not vacate
			while (A[x] != -1 && A[x] != x)
			{
				// store the value from
				// desired place
				int y = A[x];

				// place the x to its correct
				// position
				A[x] = x;

				// now y will become x, now
				// search the place for x
				x = y;
			}

			// place the x to its correct
			// position
			A[x] = x;

			// check if while loop hasn't
			// set the correct value at A[i]
			if (A[i] != i)
			{
				// if not then put -1 at
				// the vacated place
				A[i] = -1;
			}
		}
	}
}

// Driver code
int main()
{
	int A[] = { -1, -1, 6, 1, 9,
			3, 2, -1, 4, -1 };

	int len = sizeof(A) / sizeof(A[0]);

	// Function Call
	fixArray(A, len);

	// Print the output
	for (int i = 0; i < len; i++)
		printf("%d ",A[i]);
}

// This code is contributed by kothavvsaakash
