// Source: https://www.geeksforgeeks.org/given-an-array-a-and-a-number-x-check-for-pair-in-a-with-sum-as-x/

// Java Code for above Approach to tell if there exists a pair in array
// whose sum results in x.
import java.io.*;
import java.util.*;

class ON_123
{

public static int[] findSum(int arr[], int n, int target)
{
	int i, findElement;
	Map<Integer,Integer> mp=new HashMap<Integer,Integer>();
	int result[] = {0,0};
	for(i = 0; i < n; i++)
	{
	findElement = target-arr[i];
	if(mp.containsKey(findElement))
	{
		result[0] = mp.get(findElement);
		result[1] = i;
		break;
	}
	else mp.put(arr[i],i);
	}
	return result;
}

// Driver Code
public static void main(String[] args)
{
	int A[] = {1,5,4,3,7,9,2};
	int n = A.length;
	int search = 7;
	int ans[] = findSum(A,n,search);
	System.out.println(Math.min(ans[0], ans[1]) + " " +Math.max(ans[0], ans[1]));
}
}

// This code is contributed by kothavvsaakash

