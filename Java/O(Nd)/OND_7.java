import java.io.*;

class OND_7 {

// Here the size of window increases as it encounters
// positive numbers
public static void rearrangePosNegWithOrder(int[] arr)
{
	int i = 0, j = 0;
	while (j < arr.length) {
		if (arr[j] >= 0) {
			j++;
		}
		else {
			for (int k = j; k > i; k--) {
				int temp = arr[k];
				arr[k] = arr[k - 1];
				arr[k - 1] = temp;
			}
			i++;
			j++;
		}
	}
}
public static void main(String[] args)
{
	int arr[] = { -12, 11, -13, -5, 6, -7, 5, -3, -6 };

	rearrangePosNegWithOrder(arr);

	for (int i : arr) {
		System.out.print(i + " ");
	}
}
}
