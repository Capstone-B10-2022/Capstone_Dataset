// Java implementation of the above approach
//https://www.geeksforgeeks.org/find-number-of-triangles-possible/
import java.util.*;

class sq36 {
	static void CountTriangles(int[] A)
	{
		int n = A.length;

		Arrays.sort(A);

		int count = 0;

		for (int i = n - 1; i >= 1; i--) {
			int l = 0, r = i - 1;
			while (l < r) {
				if (A[l] + A[r] > A[i]) {

					// If it is possible with a[l], a[r]
					// and a[i] then it is also possible
					// with a[l+1]..a[r-1], a[r] and a[i]
					count += r - l;

					// checking for more possible solutions
					r--;
				}
				else // if not possible check for
				// higher values of arr[l]
				{
					l++;
				}
			}
		}
		System.out.print("No of possible solutions: " + count);
	}

	// Driver Code
	public static void main(String[] args)
	{
		int[] A = { 4, 3, 5, 7, 6 };

		CountTriangles(A);
	}
}

// This code is contributed by PrinciRaj1992
