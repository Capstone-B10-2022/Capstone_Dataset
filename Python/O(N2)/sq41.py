# A Simple python program to find longest common
# subarray of two binary arrays with same sum
#https://www.geeksforgeeks.org/longest-span-sum-two-binary-arrays/
# Returns length of the longest common subarray
# with same sum
def longestCommonSum(arr1, arr2, n):

	# Initialize result
	maxLen = 0

	# One by one pick all possible starting points
	# of subarrays
	for i in range(0,n):

		# Initialize sums of current subarrays
		sum1 = 0
		sum2 = 0

		# Consider all points for starting with arr[i]
		for j in range(i,n):
	
			# Update sums
			sum1 += arr1[j]
			sum2 += arr2[j]

			# If sums are same and current length is
			# more than maxLen, update maxLen
			if (sum1 == sum2):
				len = j-i+1
				if (len > maxLen):
					maxLen = len
	
	return maxLen


# Driver program to test above function
arr1 = [0, 1, 0, 1, 1, 1, 1]
arr2 = [1, 1, 1, 1, 1, 0, 1]
n = len(arr1)
print("Length of the longest common span with same "
			"sum is",longestCommonSum(arr1, arr2, n))

# This code is contributed by
# Smitha Dinesh Semwal
