// Source: https://www.geeksforgeeks.org/find-repetitive-element-1-n-1/

// Java program to find the only repeating
// element in an array where elements are
// from 1 to N-1.
class ON_128 {

	static int findRepeating(int arr[], int N)
	{

		// res is going to store value of
		// 1 ^ 2 ^ 3 .. ^ (N-1) ^ arr[0] ^
		// arr[1] ^ .... arr[n-1]
		int res = 0;
		for (int i = 0; i < N - 1; i++)
			res = res ^ (i + 1) ^ arr[i];
		res = res ^ arr[N - 1];

		return res;
	}

	// Driver code
	public static void main(String[] args)
	{
		int arr[] = { 9, 8, 2, 6, 1, 8, 5, 3, 4, 7 };
		int N = arr.length;
	
		// Function call
		System.out.println(findRepeating(arr, N));
	}
}

// This code is contributed by
// Smitha Dinesh Semwal.

