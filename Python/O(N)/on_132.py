# Source: https://www.geeksforgeeks.org/equilibrium-index-of-an-array/

# Python program for the above approach
def find(arr, n):
	mid = n // 2;
	leftSum = 0;
	rightSum = 0;

	# calculation sum to left of mid
	for i in range(mid):
		leftSum += arr[i];
	
	# calculating sum to right of mid
	for i in range(n - 1, mid, -1):
		rightSum += arr[i];
	

	# if rightsum > leftsum
	if (rightSum > leftSum):
	
		# we keep moving right until rightSum become equal or less than leftSum
		while (rightSum > leftSum and mid < n - 1):
			rightSum -= arr[mid + 1];
			leftSum += arr[mid];
			mid += 1;
		
	else:
		# we keep moving right until leftSum become equal or less than RightSum
		while (leftSum > rightSum and mid > 0):
			rightSum += arr[mid];
			leftSum -= arr[mid - 1];
			mid -= 1;
		
	# check if both sum become equal
	if (rightSum == leftSum):
		print("First Point of equilibrium is at index =" , mid);
		return;
	print("First Point of equilibrium is at index =" , -1);

# Driver code
if __name__ == '__main__':
	arr = [ 1, 1, 1, -1, 1, 1, 1 ];
	n = len(arr);
	find(arr, n);

# This code is contributed by gauravrajput1
