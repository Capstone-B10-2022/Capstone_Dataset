// Java program for rearrange an
// array such that arr[i] = i.
import java.util.*;
import java.lang.*;

public class sq6 {

	// Function to rearrange an array
	// such that arr[i] = i.
	public static int[] fix(int[] A)
	{
		for (int i = 0; i < A.length; i++)
		{
			if (A[i] != -1 && A[i] != i)
			{
				int x = A[i];

				// check if desired place
				// is not vacate
				while (A[x] != -1 && A[x] != x)
				{
					// store the value from
					// desired place
					int y = A[x];

					// place the x to its correct
					// position
					A[x] = x;

					// now y will become x, now
					// search the place for x
					x = y;
				}

				// place the x to its correct
				// position
				A[x] = x;

				// check if while loop hasn't
				// set the correct value at A[i]
				if (A[i] != i)
				{
					// if not then put -1 at
					// the vacated place
					A[i] = -1;
				}
			}
		}
		return A;
	}

	// Driver code
	public static void main(String[] args)
	{
		int A[] = { -1, -1, 6, 1, 9, 3, 2, -1, 4, -1 };
		System.out.println(Arrays.toString(fix(A)));
	}
}
