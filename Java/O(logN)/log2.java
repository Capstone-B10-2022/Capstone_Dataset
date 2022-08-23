// Java program to perform range queries over range
// queries.
//https://www.geeksforgeeks.org/array-range-queries-range-queries/
import java.io.*;
import java.util.*;
class log2
{

// Updates a node in Binary Index Tree (BITree) at given index
// in BITree. The given value 'val' is added to BITree[i] and
// all of its ancestors in tree.
static void updateBIT(int BITree[], int n, int index, int val)
{

	// index in BITree[] is 1 more than the index in arr[]
	index = index + 1;

	// Traverse all ancestors and add 'val'
	while (index <= n)
	{

	// Add 'val' to current node of BI Tree
	BITree[index] = (val + BITree[index]);

	// Update index to that of parent in update View
	index = (index + (index & (-index)));
	}
	return;
}

// Constructs and returns a Binary Indexed Tree for given
// array of size n.
static int[] constructBITree(int n)
{

	// Create and initialize BITree[] as 0
	int[] BITree = new int[n + 1];
	for (int i = 1; i <= n; i++)
	BITree[i] = 0;

	return BITree;
}

// Returns sum of arr[0..index]. This function assumes
// that the array is preprocessed and partial sums of
// array elements are stored in BITree[]
static int getSum(int BITree[], int index)
{
	int sum = 0;

	// index in BITree[] is 1 more than the index in arr[]
	index = index + 1;

	// Traverse ancestors of BITree[index]
	while (index > 0)
	{

	// Add element of BITree to sum
	sum = (sum + BITree[index]);

	// Move index to parent node in getSum View
	index -= index & (-index);
	}
	return sum;
}

// Function to update the BITree
static void update(int BITree[], int l, int r, int n, int val)
{
	updateBIT(BITree, n, l, val);
	updateBIT(BITree, n, r + 1, -val);
	return;
}

// Driver code
public static void main (String[] args)
{

	int n = 5, m = 5;
	int temp[] = { 1, 1, 2, 1, 4, 5, 2, 1, 2,
				2, 1, 3, 2, 3, 4 };
	int[][] q = new int[6][3];
	int j = 0;
	for (int i = 1; i <= m; i++) {
	q[i][0] = temp[j++];
	q[i][1] = temp[j++];
	q[i][2] = temp[j++];
	}

	// BITree for query of type 2
	int[] BITree = constructBITree(m);

	// BITree for query of type 1
	int[] BITree2 = constructBITree(n);

	// Input the queries in a 2D matrix
	/*Scanner sc=new Scanner(System.in);
		for (int i = 1; i <= m; i++)
		{
			q[i][0]=sc.nextInt();
			q[i][1]=sc.nextInt();
			q[i][2]=sc.nextInt();
		}*/

	// If query is of type 2 then function call
	// to update with BITree
	for (int i = m; i >= 1; i--)		
	if (q[i][0] == 2)
		update(BITree, q[i][1] - 1, q[i][2] - 1, m, 1);

	for (int i = m; i >= 1; i--) {
	if (q[i][0] == 2) {
		int val = getSum(BITree, i - 1);
		update(BITree, q[i][1] - 1, q[i][2] - 1, m, val);
	}
	}

	// If query is of type 1 then function call
	// to update with BITree2
	for (int i = m; i >= 1; i--) {		
	if (q[i][0] == 1) {
		int val = getSum(BITree, i - 1);
		update(BITree2, q[i][1] - 1, q[i][2] - 1,
			n, (val + 1));
	}
	}

	for (int i = 1; i <= n; i++)
	System.out.print(getSum(BITree2, i - 1)+" ");

}
}

// This code is contributed by avanitrachhadiya2155
