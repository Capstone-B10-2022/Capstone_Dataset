# Python3 code to find Two elements
# whose sum is closest to zero
# https://www.geeksforgeeks.org/two-elements-whose-sum-is-closest-to-zero/
def minAbsSumPair(arr,arr_size):
	inv_count = 0

	# Array should have at least
	# two elements
	if arr_size < 2:
		print("Invalid Input")
		return

	# Initialization of values
	min_l = 0
	min_r = 1
	min_sum = arr[0] + arr[1]
	for l in range (0, arr_size - 1):
		for r in range (l + 1, arr_size):
			sum = arr[l] + arr[r]				
			if abs(min_sum) > abs(sum):		
				min_sum = sum
				min_l = l
				min_r = r

	print("The two elements whose sum is minimum are",
			arr[min_l], "and ", arr[min_r])

# Driver program to test above function
arr = [1, 60, -10, 70, -80, 85]

minAbsSumPair(arr, 6);

# This code is contributed by Smitha Dinesh Semwal
