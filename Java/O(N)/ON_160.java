// Source: https://www.geeksforgeeks.org/check-if-array-elements-are-consecutive/

// Java implementation of the approach
import java.util.Arrays;
import java.util.Collections;

class ON_160 {
	
boolean areConsecutive(int arr[], int n)
{
	int min_ele = Arrays.stream(arr).min().getAsInt();
	int num = 0;
	for(int i=0; i<n; i++){
		num = num ^ min_ele ^ arr[i];
		min_ele += 1;
	}
	if(num == 0)
		return true;
	return false;
}

	

	public static void main(String[] args)
	{
		ON_160 consecutive = new ON_160();
		int arr[] = {5, 4, 2, 3, 1, 6};
		int n = arr.length;
		if (consecutive.areConsecutive(arr, n) == true)
			System.out.println("Array elements are consecutive");
		else
			System.out.println("Array elements are not consecutive");
	}
}

// This code is contributed by Aarti_Rathi
