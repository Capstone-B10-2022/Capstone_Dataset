//https://www.geeksforgeeks.org/find-the-minimum-distance-between-two-numbers/
// Java Program to Find the minimum
// distance between two numbers
class sq25 {
	int minDist(int arr[], int n, int x, int y)
	{
		int i, j;
		int min_dist = Integer.MAX_VALUE;
		for (i = 0; i < n; i++) {
			for (j = i + 1; j < n; j++) {
				if ((x == arr[i] && y == arr[j]
					|| y == arr[i] && x == arr[j])
					&& min_dist > Math.abs(i - j))
					min_dist = Math.abs(i - j);
			}
		}
		if (min_dist > n) {
			return -1;
		}
		return min_dist;
	}

	public static void main(String[] args)
	{
		sq25 min = new sq25();
		int arr[] = { 3, 5, 4, 2, 6, 5, 6, 6, 5, 4, 8, 3 };
		int n = arr.length;
		int x = 0;
		int y = 6;

		System.out.println("Minimum distance between " + x
						+ " and " + y + " is "
						+ min.minDist(arr, n, x, y));
	}
}
