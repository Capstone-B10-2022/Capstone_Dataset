// Java program to rearrange positive
// and negative numbers
import java.io.*;

class sq11 {

static void rearrange(int a[], int size)
{
int positive = 0, negative = 1, temp;

	while (true) {

	/* Move forward the positive pointer till
	negative number number not encountered */
	while (positive < size && a[positive] >= 0)
		positive += 2;

	/* Move forward the negative pointer till
		positive number number not encountered */
	while (negative < size && a[negative] <= 0)
		negative += 2;

	// Swap array elements to fix their position.
	if (positive < size && negative < size) {
		temp = a[positive];
		a[positive] = a[negative];
		a[negative] = temp;
	}

	/* Break from the while loop when any index
	exceeds the size of the array */
	else
		break;
	}
}

// Driver code
public static void main(String args[]) {
	int arr[] = {1, -3, 5, 6, -3, 6, 7, -4, 9, 10};
	int n = arr.length;

	rearrange(arr, n);
	for (int i = 0; i < n; i++)
	System.out.print(arr[i] + " ");
}
}

/*This code is contributed by Nikita Tiwari.*/
