// Source: geeksforgeeks.org/find-the-two-repeating-elements-in-a-given-array/

class ON_146
{
	void printRepeating(int arr[], int size)
	{
		/* Will hold xor of all elements */
		int xor = arr[0];
		
		/* Will have only single set bit of xor */
		int set_bit_no;
		
		int i;
		int n = size - 2;
		int x = 0, y = 0;

		/* Get the xor of all elements in arr[] and {1, 2 .. n} */
		for (i = 1; i < size; i++)
			xor ^= arr[i];
		for (i = 1; i <= n; i++)
			xor ^= i;

		/* Get the rightmost set bit in set_bit_no */
		set_bit_no = (xor & ~(xor - 1));

		/* Now divide elements in two sets by comparing rightmost set
		bit of xor with bit at same position in each element. */
		for (i = 0; i < size; i++) {
			int a = arr[i] & set_bit_no;
			if (a != 0)
				x = x ^ arr[i]; /*XOR of first set in arr[] */
			else
				y = y ^ arr[i]; /*XOR of second set in arr[] */
		}
		for (i = 1; i <= n; i++)
		{
			int a = i & set_bit_no;
			if (a != 0)
				x = x ^ i; /*XOR of first set in arr[] and {1, 2, ...n }*/
			else
				y = y ^ i; /*XOR of second set in arr[] and {1, 2, ...n } */
		}

		System.out.println("The two reppeated elements are :");
		System.out.println(x + " " + y);
	}

	/* Driver program to test the above function */
	public static void main(String[] args)
	{
		ON_146 repeat = new ON_146();
		int arr[] = {4, 2, 4, 5, 2, 3, 1};
		int arr_size = arr.length;
		repeat.printRepeating(arr, arr_size);
	}
}

// This code has been contributed by Mayank Jaiswal

