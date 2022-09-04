# Source: https://www.geeksforgeeks.org/find-maximum-average-subarray-of-k-length/

# Python program to find maximum average subarray
# of given length.

# Returns beginning index of maximum average
# subarray of length 'k'
def findMaxAverage(arr, n, k):
	# Check if 'k' is valid
	if k > n:
		return -1

	# Create and fill array to store cumulative
	# sum. csum[i] stores sum of arr[0] to arr[i]
	csum = [0]*n
	csum[0] = arr[0]
	for i in range(1, n):
		csum[i] = csum[i-1] + arr[i];

	# Initialize max_sm as sum of first subarray
	max_sum = csum[k-1]
	max_end = k-1

	# Find sum of other subarrays and update
	# max_sum if required.
	for i in range(k, n):
	
		curr_sum = csum[i] - csum[i-k]
		if curr_sum > max_sum:
		
			max_sum = curr_sum
			max_end = i
		
	# Return starting index
	return max_end - k + 1

# Driver program
arr = [1, 12, -5, -6, 50, 3]
k = 4
n = len(arr)
print("The maximum average subarray of length",k,
"begins at index",findMaxAverage(arr, n, k))

#This code is contributed by
#Smitha Dinesh Semwal

