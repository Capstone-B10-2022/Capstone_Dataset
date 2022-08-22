// Java code to reorder an array
// according to given indices
class nlog1{
	
static int heapSize;

public static void heapify(int arr[],
						int index[], int i)
{
	int largest = i;
	
	// left child in 0 based indexing
	int left = 2 * i + 1;
	
	// right child in 1 based indexing
	int right = 2 * i + 2;
	
	// Find largest index from root,
	// left and right child
	if (left < heapSize &&
		index[left] > index[largest] )
	{
		largest = left;
	}
	if (right < heapSize &&
		index[right] > index[largest] )
	{
		largest = right;
	}
	
	if (largest != i)
	{
		
		// swap arr whenever index is swapped
		int temp = arr[largest];
		arr[largest] = arr[i];
		arr[i] = temp;
		
		temp = index[largest];
		index[largest] = index[i];
		index[i] = temp;
		
		heapify(arr, index, largest);
	}
}

public static void heapSort(int arr[],
							int index[], int n)
{
	
	// Build heap
	for(int i = (n - 1) / 2 ; i >= 0 ; i--)
	{
		heapify(arr, index, i);
	}
	
	// Swap the largest element of
	// index(first element)
	// with the last element
	for(int i = n - 1 ; i > 0 ; i--)
	{
		int temp = index[0];
		index[0] = index[i];
		index[i] = temp;
		
		// swap arr whenever index is swapped
		temp = arr[0];
		arr[0] = arr[i];
		arr[i] = temp;
		
		heapSize--;
		heapify(arr, index, 0);
	}
}

// Driver code
public static void main(String[] args)
{
	int arr[] = { 50, 40, 70, 60, 90 };
	int index[] = { 3, 0, 4, 1, 2 };
	int n = arr.length;
	
	heapSize = n;
	heapSort(arr, index, n);
	
	System.out.println("Reordered array is: ");
	for(int i = 0 ; i < n ; i++)
		System.out.print(arr[i] + " ");
		
	System.out.println();
	
	System.out.println("Modified Index array is: ");
	for(int i = 0; i < n; i++)
		System.out.print(index[i] + " ");
}
}

// This code is contributed by divyeshrabadiya07
