// Java program for the above approach
//https://www.geeksforgeeks.org/java-program-to-find-the-mth-element-of-the-array-after-k-left-rotations/
import java.util.*;
class on2{
	
// Function to return Mth element of
// array after k left rotations
public static int getFirstElement(int[] a, int N,
								int K, int M)
{
	
	// The array comes to original state
	// after N rotations
	K %= N;

	// Mth element after k left rotations
	// is (K+M-1)%N th element of the
	// original array
	int index = (K + M - 1) % N;

	int result = a[index];

	// Return the result
	return result;
}

// Driver code
public static void main(String[] args)
{
	
	// Array initialization
	int a[] = { 3, 4, 5, 23 };

	// Size of the array
	int N = a.length;

	// Given K rotation and Mth element
	// to be found after K rotation
	int K = 2, M = 1;

	// Function call
	System.out.println(getFirstElement(a, N, K, M));
}
}

// This code is contributed by divyeshrabadiya07
