// Java program to check if there exists a pair
// in array whose sum results in x.
//https://www.geeksforgeeks.org/given-an-array-a-and-a-number-x-check-for-pair-in-a-with-sum-as-x/
class sq39{

// Function to find and print pair
static boolean chkPair(int A[], int size, int x) {
	for (int i = 0; i < (size - 1); i++) {
		for (int j = (i + 1); j < size; j++) {
			if (A[i] + A[j] == x) {
				System.out.println("Pair with a given sum " + x +
									" is (" + A[i] + ", " + A[j] + ")");

				return true;
			}
		}
	}

	return false;
}

public static void main(String [] args) {
	
	int A[] = {0, -1, 2, -3, 1};
	int x = -2;
	int size = A.length;

	if (chkPair(A, size, x)) {
		System.out.println("Valid pair exists");
	}
	else {
		System.out.println("No valid pair exists for " + x );
	}
}
}

// This code is contributed by umadevi9616
