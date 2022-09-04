// Source: https://www.geeksforgeeks.org/find-the-minimum-distance-between-two-numbers/

// Java program to Find the minimum
// distance between two numbers

public class ON_98 {

	static int minDist(int arr[], int n, int x, int y)
	{
		// idx1 and idx2 will store indices of
		// x or y and min_dist will store the minimum
		// difference
		int idx1 = -1, idx2 = -1,
			min_dist = Integer.MAX_VALUE;
		for (int i = 0; i < n; i++) {
			// if current element is x then change idx1
			if (arr[i] == x) {
				idx1 = i;
			}
			// if current element is y then change idx2
			else if (arr[i] == y) {
				idx2 = i;
			}
			// if x and y both found in array
			// then only find the difference and store it in
			// min_dist
			if (idx1 != -1 && idx2 != -1)
				min_dist = Math.min(min_dist,
									Math.abs(idx1 - idx2));
		}

		// if left or right did not found in array
		// then return -1
		if (idx1 == -1 || idx2 == -1)
			return -1;
		// return the minimum distance
		else
			return min_dist;
	}

	/* Driver code */
	public static void main(String[] args)
	{
		int arr[] = { 3, 5, 4, 2, 6, 5, 6, 6, 5, 4, 8, 3 };
		int n = arr.length;
		int x = 3;
		int y = 6;

		System.out.println("Minimum distance between " + x
						+ " and " + y + " is "
						+ minDist(arr, n, x, y));
	}
}

// This code is contributed by Lovely Jain
