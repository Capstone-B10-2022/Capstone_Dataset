// Source: https://www.geeksforgeeks.org/equilibrium-index-of-an-array/

// Java program for the above approach
import java.io.*;
import java.util.*;

class ON_135{

static void find(int arr[], int n)
{
	int mid = n / 2;
	int leftSum = 0, rightSum = 0;

	//calculation sum to left of mid
	for (int i = 0; i < mid; i++)
	{
		leftSum += arr[i];
	}
	//calculating sum to right of mid
	for (int i = n - 1; i > mid; i--)
	{
		rightSum += arr[i];
	}

	//if rightsum > leftsum
	if (rightSum > leftSum)
	{
		//we keep moving right until rightSum become equal or less than leftSum
		while (rightSum > leftSum && mid < n - 1)
		{
			rightSum -= arr[mid + 1];
			leftSum += arr[mid];
			mid++;
		}
	}
	else
	{
		//we keep moving right until leftSum become equal or less than RightSum
		while (leftSum > rightSum && mid > 0)
		{
			rightSum += arr[mid];
			leftSum -= arr[mid - 1];
			mid--;
		}
	}

	//check if both sum become equal
	if (rightSum == leftSum)
	{
		System.out.print("First Point of equilibrium is at index ="+ mid);
		return;
	}

	System.out.print("First Point of equilibrium is at index =" + -1);
}

// Driver code
public static void main(String args[])
{
	int arr[] = { 1,1,1,-1,1,1,1 };
	int n = arr.length;
	find(arr, n);
}
}

