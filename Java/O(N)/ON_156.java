// Source: https://www.geeksforgeeks.org/a-product-array-puzzle/


// Java program for the above approach
import java.io.*;
import java.util.*;

class ON_156 {

	public static long[] productExceptSelf(int a[], int n)
	{
		long prod = 1;
		long flag = 0;

		// product of all elements
		for (int i = 0; i < n; i++) {

			// counting number of elements
			// which have value
			// 0
			if (a[i] == 0)
				flag++;
			else
				prod *= a[i];
		}

		// creating a new array of size n
		long arr[] = new long[n];
		for (int i = 0; i < n; i++) {

			// if number of elements in
			// array with value 0
			// is more than 1 than each
			// value in new array
			// will be equal to 0
			if (flag > 1) {
				arr[i] = 0;
			}

			// if no element having value
			// 0 than we will
			// insert product/a[i] in new array
			else if (flag == 0)
				arr[i] = (prod / a[i]);

			// if 1 element of array having
			// value 0 than all
			// the elements except that index
			// value , will be
			// equal to 0
			else if (flag == 1 && a[i] != 0) {
				arr[i] = 0;
			}

			// if(flag == 1 && a[i] == 0)
			else
				arr[i] = prod;
		}
		return arr;
	}

	// Driver Code
	public static void main(String args[])
		throws IOException
	{
		int n = 5;
		int[] array = { 10, 3, 5, 6, 2 };

		ON_156 ob = new ON_156();
		long[] ans = new long[n];
		ans = ob.productExceptSelf(array, n);

		for (int i = 0; i < n; i++) {
			System.out.print(ans[i] + " ");
		}
	}
}

// This code is contributed by Kapil Kumar (kapilkumar2001)

