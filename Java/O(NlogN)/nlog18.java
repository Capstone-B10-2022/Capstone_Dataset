// Given an array of numbers,
// program to arrange the numbers
// to form the largest number
import java.util.*;

public class nlog18
{

// The main function that prints
// the arrangement with the
// largest value. The function
// accepts a vector of strings
static void printLargest(ArrayList<Integer> arr)
{

	// Sort the numbers using
	// library sort function. The
	// function uses our comparison
	// function myCompare() to
	// compare two strings.
	Collections.sort(arr, new Comparator<Integer>(){

	// A comparison function which
	// is used by sort() in
	// printLargest()
	@Override
	public int compare(Integer x, Integer y)
	{

		int xy = x;
		int yx = y;

		// Count length of x and y
		int countx = 0;
		int county = 0;

		// Count length of X
		while (x > 0) {
		countx++;
		x /= 10;
		}

		// Count length of Y
		while (y > 0) {
		county++;
		y /= 10;
		}

		x = xy;
		y = yx;

		while (countx > 0)
		{
		countx--;
		yx *= 10;
		}

		while (county > 0)
		{
		county--;
		xy *= 10;
		}

		// Append x to y
		yx += x;

		// Append y to x
		xy += y;

		return -xy + yx;
	}
	});

	for (int i = 0; i < arr.size(); i++)
	System.out.print(arr.get(i));
}

// Driver code
public static void main(String[] args)
{
	// Output should be 6054854654
	ArrayList<Integer> arr = new ArrayList<>();
	arr.add(54);
	arr.add(546);
	arr.add(548);
	arr.add(60);

	printLargest(arr);

}
}

// this code is contributed by phasing17
