// Java program to find distinct elements
// common to all rows of a matrix
//https://www.geeksforgeeks.org/find-distinct-elements-common-rows-matrix/
import java.util.*;
class sq53{

static int MAX = 100;

// function to individually sort
// each row in increasing order
@SuppressWarnings("unchecked")
static void findAndPrintCommonElements(int mat[][], int n)
{
	HashSet<Integer> us = new HashSet<Integer>();

	// map elements of first row
	// into 'us'
	for (int i = 0; i < n; i++)
	us.add(mat[0][i]);

	for (int i = 1; i < n; i++)
	{
	HashSet<Integer> temp = new HashSet<Integer>();

	// mapping elements of current row
	// in 'temp'
	for (int j = 0; j < n; j++)
		temp.add(mat[i][j]);

	HashSet<Integer> itr=(HashSet<Integer>) us.clone();

	// iterate through all the elements
	// of 'us'
	for (int x :itr)

		// if an element of 'us' is not present
		// into 'temp', then erase that element
		// from 'us'
		if (!temp.contains(x))
		us.remove(x);

	// if size of 'us' becomes 0,
	// then there are no common elements
	if (us.size() == 0)
		break;
	}

	// print the common elements
	HashSet<Integer> itr1=(HashSet<Integer>) us.clone();
	for (int x :itr1)
	System.out.print(x+ " ");
}

// Driver program to test above
public static void main(String[] args)
{
	int mat[][] = { {2, 1, 4, 3},
				{1, 2, 3, 2},
				{3, 6, 2, 3},
				{5, 2, 5, 3} };
	int n = 4;
	findAndPrintCommonElements(mat, n);
}
}

// This code is contributed by shikhasingrajput
