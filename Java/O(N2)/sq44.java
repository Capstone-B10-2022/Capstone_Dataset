//https://www.geeksforgeeks.org/find-subarray-with-given-sum/
class sq44{
	/* Returns true if the there is a
subarray of arr[] with a sum equal to
	'sum' otherwise returns false.
Also, prints the result */
	void subArraySum(int arr[], int n, int sum)
	{
		int currentSum, i, j;

		// Pick a starting point
		for (i = 0; i < n; i++) {
			currentSum = arr[i];

			// try all subarrays starting with 'i'
			for (j = i + 1; j <= n; j++) {
				if (currentSum == sum) {
					int p = j - 1;
					System.out.println(
						"Sum found between indexes " + i
						+ " and " + p);
					return;
				}
				if (currentSum > sum || j == n)
					break;
				currentSum = currentSum + arr[j];
			}
		}

		System.out.println("No subarray found");
		return;
	}

	public static void main(String[] args)
	{
		sq44 arraysum = new sq44();
		int arr[] = { 15, 2, 4, 8, 9, 5, 10, 23 };
		int n = arr.length;
		int sum = 23;
		arraysum.subArraySum(arr, n, sum);
	}
}

// This code has been contributed by Mayank
// Jaiswal(mayank_24)
