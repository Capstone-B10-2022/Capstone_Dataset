// Source: https://www.geeksforgeeks.org/check-array-majority-element/

// Hashing based Java program
// to find if there is a
// majority element in input array.
import java.util.*;
import java.lang.*;
import java.io.*;

class ON_141
{
	// Returns true if there is a
	// majority element in a[]
	static boolean isMajority(int a[], int n)
	{
		// Insert all elements
		// in a hash table
		HashMap <Integer,Integer> mp = new
							HashMap<Integer,Integer>();
		
		for (int i = 0; i < n; i++)
		
			if (mp.containsKey(a[i]))
				mp.put(a[i], mp.get(a[i]) + 1);
		
			else mp.put(a[i] , 1);
		
		// Check if frequency of any
		// element is n/2 or more.
		for (Map.Entry<Integer, Integer> x : mp.entrySet())
			
			if (x.getValue() >= n/2)
				return true;
		return false;
	}
	
	// Driver code
	public static void main (String[] args)
	{
		int a[] = { 2, 3, 9, 2, 2 };
		int n = a.length;
		
		if (isMajority(a, n))
			System.out.println("Yes");
		else
			System.out.println("No");
	}
}

// This code is contributed by Ansu Kumari

