// Java code to minimize number of rotations
//https://www.geeksforgeeks.org/minimize-number-of-rotations-on-array-a-such-that-it-becomes-equal-to-b/
import java.util.*;
public class sq23
{

// Function to check if two arrays are equal
static boolean check(int A[], int B[], int N)
{
	boolean flag = true;
	for (int i = 0; i < N; i++) {
		if (A[i] != B[i]) {
			flag = false;
			break;
		}
	}
	return flag;
}

// Function to left rotate an array
static void Leftrotate(int A[], int N)
{
	int temp = A[0];
	for (int i = 0; i < N - 1; i++) {
		A[i] = A[i + 1];
	}
	A[N - 1] = temp;
}

// Function to right rotate an array
static void Rightrotate(int A[], int N)
{
	int temp = A[N - 1];
	for (int i = N - 1; i > 0; i--) {
		A[i] = A[i - 1];
	}
	A[0] = temp;
}

// Function to minimize number of rotations
static int minRotations(int A[], int B[], int N)
{
	int C[] = new int[N];
	for (int i = 0; i < N; i++)
		C[i] = A[i];
	int a = 0, b = 0;

	// Right rotate the array
	// till it is equal to B
	while (check(A, B, N) == false) {
		Rightrotate(A, N);
		a++;
	}

	// Left rotate the array
	// till it is equal to B
	while (check(C, B, N) == false) {
		Leftrotate(C, N);
		b++;
	}

	int ans = Math.min(a, b);
	return ans;
}

// Driver code
public static void main(String args[])
{
	int A[] = { 13, 12, 7, 18, 4, 5, 1 };
	int B[] = { 12, 7, 18, 4, 5, 1, 13 };
	int N = A.length;

	int ans = minRotations(A, B, N);
	System.out.println(ans);

}
}

// This code is contributed by Samim Hossain Mondal.
