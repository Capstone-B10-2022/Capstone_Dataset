// Source: geeksforgeeks.org/find-the-two-repeating-elements-in-a-given-array/

class ON_144
{
	void printRepeating(int arr[], int size)
	{
		int count[] = new int[size];
		int i;

		System.out.println("Repeated elements are : ");
		for (i = 0; i < size; i++)
		{
			if (count[arr[i]] == 1)
				System.out.print(arr[i] + " ");
			else
				count[arr[i]]++;
		}
	}

	public static void main(String[] args)
	{
		ON_144 repeat = new ON_144();
		int arr[] = {4, 2, 4, 5, 2, 3, 1};
		int arr_size = arr.length;
		repeat.printRepeating(arr, arr_size);
	}
}

