// Java code to move matrix
// elements in given direction
// with add element with same value
//https://www.geeksforgeeks.org/move-matrix-elements-given-direction-add-elements-value/
import java.io.*;
import java.util.*;

class sq59 {
	// Function to shift the matrix
	// in the given direction
	static void moveMatrix(char d,
						int n,
						int a[][])
	{

		// For right shift move.
		if (d == 'r') {

			// for each row from
			// top to bottom
			for (int i = 0; i < n; i++) {
				ArrayList<Integer> v = new ArrayList<Integer>();
				ArrayList<Integer> w = new ArrayList<Integer>();
				int j;

				// for each element of
				// row from right to left
				for (j = n - 1; j >= 0; j--) {
					// if not 0
					if (a[i][j] != 0)
						v.add(a[i][j]);
				}

				// for each temporary array
				for (j = 0; j < v.size(); j++) {
					// if two element have
					// same value at
					// consecutive position.
					if (j < v.size() - 1 && v.get(j) == v.get(j + 1)) {
						// insert only one element
						// as sum of two same element.
						w.add(2 * v.get(j));
						j++;
					}
					else
						w.add(v.get(j));
				}

				// filling the each
				// row element to 0.
				for (j = 0; j < n; j++)
					a[i][j] = 0;

				j = n - 1;

				// Copying the temporary
				// array to the current row.
				for (int it = 0; it < w.size(); it++)
					a[i][j--] = w.get(it);
			}
		}

		// for left shift move
		else if (d == 'l') {

			// for each row
			for (int i = 0; i < n; i++) {
				ArrayList<Integer> v = new ArrayList<Integer>();
				ArrayList<Integer> w = new ArrayList<Integer>();
				int j;

				// for each element of the
				// row from left to right
				for (j = 0; j < n; j++) {
					// if not 0
					if (a[i][j] != 0)
						v.add(a[i][j]);
				}

				// for each temporary array
				for (j = 0; j < v.size(); j++) {
					// if two element have
					// same value at
					// consecutive position.
					if (j < v.size() - 1 && v.get(j) == v.get(j + 1)) {
						// insert only one
						// element as sum
						// of two same element.
						w.add(2 * v.get(j));
						j++;
					}
					else
						w.add(v.get(j));
				}

				// filling the each
				// row element to 0.
				for (j = 0; j < n; j++)
					a[i][j] = 0;

				j = 0;

				for (int it = 0; it < w.size(); it++)
					a[i][j++] = w.get(it);
			}
		}

		// for down shift move.
		else if (d == 'd') {
			// for each column
			for (int i = 0; i < n; i++) {
				ArrayList<Integer> v = new ArrayList<Integer>();
				ArrayList<Integer> w = new ArrayList<Integer>();
				int j;

				// for each element of
				// column from bottom to top
				for (j = n - 1; j >= 0; j--) {
					// if not 0
					if (a[j][i] != 0)
						v.add(a[j][i]);
				}

				// for each temporary array
				for (j = 0; j < v.size(); j++) {

					// if two element have
					// same value at consecutive
					// position.
					if (j < v.size() - 1 && v.get(j) == v.get(j + 1)) {
						// insert only one element
						// as sum of two same element.
						w.add(2 * v.get(j));
						j++;
					}
					else
						w.add(v.get(j));
				}

				// filling the each
				// column element to 0.
				for (j = 0; j < n; j++)
					a[j][i] = 0;

				j = n - 1;

				// Copying the temporary array
				// to the current column
				for (int it = 0; it < w.size(); it++)
					a[j--][i] = w.get(it);
			}
		}

		// for up shift move
		else if (d == 'u') {
			// for each column
			for (int i = 0; i < n; i++) {
				ArrayList<Integer> v = new ArrayList<Integer>();
				ArrayList<Integer> w = new ArrayList<Integer>();
				int j;

				// for each element of column
				// from top to bottom
				for (j = 0; j < n; j++) {
					// if not 0
					if (a[j][i] != 0)
						v.add(a[j][i]);
				}

				// for each temporary array
				for (j = 0; j < v.size(); j++) {
					// if two element have
					// same value at
					// consecutive position.
					if (j < v.size() - 1 && v.get(j) == v.get(j + 1)) {
						// insert only one element
						// as sum of two same element.
						w.add(2 * v.get(j));
						j++;
					}
					else
						w.add(v.get(j));
				}

				// filling the each
				// column element to 0.
				for (j = 0; j < n; j++)
					a[j][i] = 0;

				j = 0;

				// Copying the temporary
				// array to the current
				// column
				for (int it = 0; it < w.size(); it++)
					a[j++][i] = w.get(it);
			}
		}
	}

	// Driver Code
	public static void main(String args[])
	{
		char d = 'l';
		int n = 5;
		int a[][] = { { 32, 3, 3, 3, 3 },
					{ 0, 0, 1, 0, 0 },
					{ 10, 10, 8, 1, 2 },
					{ 0, 0, 0, 0, 1 },
					{ 4, 5, 6, 7, 8 } };

		moveMatrix(d, n, a);

		// Printing the
		// final array
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < n; j++)
				System.out.print(a[i][j] + " ");

			System.out.println();
		}
	}
}

// This code is contributed by
// Manish Shaw(manishshaw1)
