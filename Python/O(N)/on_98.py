# Source: https://www.geeksforgeeks.org/find-maximum-average-subarray-of-k-length/

# Python 3 program to find maximum
# average subarray of given length.

# Returns beginning index of maximum
# average subarray of length 'k'
def findMaxAverage(arr, n, k):

	# Check if 'k' is valid
	if (k > n):
		return -1

	# Compute sum of first 'k' elements
	sum = arr[0]
	
	for i in range(1, k):
		sum += arr[i]

	max_sum = sum
	max_end = k - 1

	# Compute sum of remaining subarrays
	for i in range(k, n):
	
		sum = sum + arr[i] - arr[i - k]
		
		if (sum > max_sum):
		
			max_sum = sum
			max_end = i
		
	# Return starting index
	return max_end - k + 1

# Driver program
arr = [1, 12, -5, -6, 50, 3]
k = 4
n = len(arr)

print("The maximum average subarray of length", k,
								"begins at index",
						findMaxAverage(arr, n, k))

# This code is contributed by
# Smitha Dinesh Semwal
