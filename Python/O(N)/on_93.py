# Source: https://www.geeksforgeeks.org/find-subarray-least-average/

# Python3 program to find
# minimum average subarray

# Prints beginning and ending
# indexes of subarray of size k
# with minimum average
def findMinAvgSubarray(arr, n, k):

	# k must be smaller than or equal to n
	if (n < k): return 0

	# Initialize beginning index of result
	res_index = 0

	# Compute sum of first subarray of size k
	curr_sum = 0
	for i in range(k):
		curr_sum += arr[i]

	# Initialize minimum sum as current sum
	min_sum = curr_sum

	# Traverse from (k + 1)'th
	# element to n'th element
	for i in range(k, n):
	
		# Add current item and remove first
		# item of previous subarray
		curr_sum += arr[i] - arr[i-k]

		# Update result if needed
		if (curr_sum < min_sum):
		
			min_sum = curr_sum
			res_index = (i - k + 1)
		
	print("Subarray between [", res_index,
		", ", (res_index + k - 1),
		"] has minimum average")

# Driver Code
arr = [3, 7, 90, 20, 10, 50, 40]
k = 3 # Subarray size
n = len(arr)
findMinAvgSubarray(arr, n, k)

# This code is contributed by Anant Agarwal.
