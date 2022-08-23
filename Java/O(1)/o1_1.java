// Java program to implement
// the above approach
//https://www.geeksforgeeks.org/java-program-to-find-mth-element-after-k-right-rotations-of-an-array/
class on1{

// Function to return Mth element of
// array after k right rotations
static int getFirstElement(int a[], int N,
						int K, int M)
{
	// The array comes to original state
	// after N rotations
	K %= N;
	int index;

	// If K is greater or equal to M
	if (K >= M)

		// Mth element after k right
		// rotations is (N-K)+(M-1) th
		// element of the array
		index = (N - K) + (M - 1);

	// Otherwise
	else

		// (M - K - 1) th element
		// of the array
		index = (M - K - 1);

	int result = a[index];

	// Return the result
	return result;
}

// Driver Code
public static void main(String[] args)
{
	int a[] = { 1, 2, 3, 4, 5 };
	
	int N = 5;
	
	int K = 3, M = 2;
	
	System.out.println(getFirstElement(a, N, K, M));
}
}

// This code is contributed by Ritik Bansal
