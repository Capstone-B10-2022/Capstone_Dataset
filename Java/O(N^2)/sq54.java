// JAVA Code to find distinct elements
// common to all rows of a matrix
//https://www.geeksforgeeks.org/find-distinct-elements-common-rows-matrix/
import java.io.*;
import java.util.*;

class sq54 {
static void distinct(int matrix[][], int N)
{
	// make a empty map
	Map<Integer, Integer> ans = new HashMap<>();

	// Insert the elements of
	// first row in the map and
	// initialize with 1
	for (int j = 0; j < N; j++) {
	ans.put(matrix[0][j], 1);
	}

	// Traverse the matrix from 2nd row
	for (int i = 1; i < N; i++) {
	for (int j = 0; j < N; j++) {

		// If the element is present in the map
		// and is not duplicated in the current row
		if (ans.get(matrix[i][j]) != null
			&& ans.get(matrix[i][j]) == i) {

		// Increment count of the element in
		// map by 1
		ans.put(matrix[i][j], i + 1);

		// If we have reached the last row
		if (i == N - 1) {

			// Print the element
			System.out.print(matrix[i][j]
							+ " ");
		}
		}
	}
	}
}

/* Driver program to test above function */
public static void main(String[] args)
{
	int matrix[][] = { { 2, 1, 4, 3 },
					{ 1, 2, 3, 2 },
					{ 3, 6, 2, 3 },
					{ 5, 2, 5, 3 } };
	int n = 4;
	distinct(matrix, n);
}
}
// This code is Contributed by Darshit Shukla
