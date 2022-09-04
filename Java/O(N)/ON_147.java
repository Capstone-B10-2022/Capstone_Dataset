// Source: geeksforgeeks.org/find-the-two-repeating-elements-in-a-given-array/


class ON_147
{
	void printRepeating(int arr[], int size)
	{
		int i;
		System.out.println("The repeating elements are : ");
	
		for(i = 0; i < size; i++)
		{
		int abs_val = Math.abs(arr[i]);
			if(arr[abs_val] > 0)
				arr[abs_val] = -arr[abs_val];
			else
				System.out.print(abs_val + " ");
		}		
	}

	/* Driver program to test the above function */
	public static void main(String[] args)
	{
		ON_147 repeat = new ON_147();
		int arr[] = {4, 2, 4, 5, 2, 3, 1};
		int arr_size = arr.length;
		repeat.printRepeating(arr, arr_size);
	}
}

// This code has been contributed by Mayank Jaiswal
