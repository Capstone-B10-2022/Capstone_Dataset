// Source: https://www.geeksforgeeks.org/array-range-queries-elements-frequency-value/

/* Java Program to answer Q queries to
find number of times an element x
appears x times in a Query subarray */
import java.util.HashMap;
import java.util.Map;

class GFG
{


/* Returns the count of number x with
frequency x in the subarray from
start to end */
static int solveQuery(int start, int end, int arr[])
{
	// map for frequency of elements
	Map<Integer,Integer> mp = new HashMap<>();

	// store frequency of each element
	// in arr[start; end]
	for (int i = start; i <= end; i++)
		mp.put(arr[i],mp.get(arr[i]) == null?1:mp.get(arr[i])+1);

	// Count elements with same frequency
	// as value
	int count = 0;
	for (Map.Entry<Integer,Integer> entry : mp.entrySet())
		if (entry.getKey() == entry.getValue())
			count++;
	return count;
}

// Driver code
public static void main(String[] args)
{
	int A[] = { 1, 2, 2, 3, 3, 3 };
	int n = A.length;

	// 2D array of queries with 2 columns
	int [][]queries = { { 0, 1 },
						{ 1, 1 },
						{ 0, 2 },
						{ 1, 3 },
						{ 3, 5 },
						{ 0, 5 } };

	// calculating number of queries
	int q = queries.length;

	for (int i = 0; i < q; i++)
	{
		int start = queries[i][0];
		int end = queries[i][1];
		System.out.println("Answer for Query " + (i + 1)
			+ " = " + solveQuery(start,
			end, A));
	}
}
}

// This code is contributed by Rajput-Ji

