// Java program to implement the
// above approach
import java.io.*;
class sq7{

static void printArray(int[] array, int length)
{
System.out.print("[");

for (int i = 0; i < length; i++)
{
	System.out.print(array[i]);

	if (i < (length - 1))
	System.out.print(",");
	else
	System.out.print("]\n");
}
}

static void reverse(int[] array,
					int start,
					int end)
{
while (start < end)
{
	int temp = array[start];
	array[start] = array[end];
	array[end] = temp;
	start++;
	end--;
}
}

// Rearrange the array with
// all negative integers on left
// and positive integers on right
// use recursion to split the
// array with first element
// as one half and the rest
// array as another and then
// merge it with head of
// the array in each step
static void rearrange(int[] array,
					int start,
					int end)
{
// exit condition
if (start == end)
	return;

// rearrange the array
// except the first element
// in each recursive call
rearrange(array,
			(start + 1), end);

// If the first element of
// the array is positive,
// then right-rotate the
// array by one place first
// and then reverse the merged array.
if (array[start] >= 0)
{
	reverse(array,
			(start + 1), end);
	reverse(array,
			start, end);
}
}

// Driver code
public static void main(String[] args)
{

int[] array = {-12, -11, -13,
				-5, -6, 7, 5, 3, 6};
int length = array.length;
int countNegative = 0;

for (int i = 0; i < length; i++)
{
	if (array[i] < 0)
	countNegative++;
}

System.out.print("array: ");
printArray(array, length);
rearrange(array, 0,
		(length - 1));
reverse(array, countNegative,
		(length - 1));
System.out.print("rearranged array: ");
printArray(array, length);
}
}

// This code is contributed by Chitranayal
