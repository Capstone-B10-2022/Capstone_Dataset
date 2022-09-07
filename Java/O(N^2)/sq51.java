//https://www.geeksforgeeks.org/rotate-matrix-90-degree-without-using-extra-space-set-2/
import java.util.*;

class sq51{
	private static int[][] swap(int[][] matrix, int x1,int x2,int y1, int y2) {
		int temp = matrix[x1][x2] ;
		matrix[x1][x2] = matrix[y1][y2];
		matrix[y1][y2] = temp;
		return matrix;
		}

//Function to rotate matrix anticlockwise by 90 degrees.
static int[][] rotateby90(int[][] matrix)
{
	int n=matrix.length;
	int mid;
	if(n % 2 == 0)
		mid = n / 2 - 1;
	else
		mid = n / 2;
	for(int i = 0, j = n - 1; i <= mid; i++, j--)
	{
		for(int k = 0; k < j - i; k++)
		{
			matrix= swap(matrix, i, j - k, j, i + k);	 //ru ld
			matrix= swap(matrix, i + k, i, j, i + k);	 //lu ld
			matrix= swap(matrix, i, j - k, j - k, j);	 //ru rd
		}
	}
	return matrix;
}

static void printMatrix(int[][] arr)
{

int n = arr.length;
for(int i = 0; i < n; i++)
{
	for(int j = 0; j < n; j++)
	{
		System.out.print(arr[i][j] + " ");
	}
	System.out.println();
}
}
public static void main(String[] args) {
	
	int[][] arr = { { 1, 2, 3, 4 },
					{ 5, 6, 7, 8 },
					{ 9, 10, 11, 12 },
					{ 13, 14, 15, 16 } };
	arr = rotateby90(arr);
	printMatrix(arr);
}
}

// This code is contributed by umadevi9616
