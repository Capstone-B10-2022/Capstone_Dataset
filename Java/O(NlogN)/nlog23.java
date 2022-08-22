// Java program to find minimum product of
// k elements in an array

import java.util.PriorityQueue;

class GFG
{
	public static int minProduct(int[] arr, int n, int k)
	{
		PriorityQueue<Integer> pq = new PriorityQueue<>();
		for (int i = 0; i < n; i++)
			pq.add(arr[i]);
		
			int count = 0, ans = 1;

			// One by one extract items
			while(pq.isEmpty() == false && count < k)
			{
				ans = ans * pq.element();
				pq.remove();
				count++;
			}
		
			return ans;
	}

	// Driver Code
	public static void main(String[] args)
	{
		int arr[] = {198, 76, 544, 123, 154, 675};
		int k = 2;
		int n = arr.length;
		System.out.print("Minimum product is " +
						minProduct(arr, n, k));
	}
}

// This code is contributed by sanjeev2552
