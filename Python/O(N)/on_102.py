# Source: https://www.geeksforgeeks.org/longest-span-sum-two-binary-arrays/

# Python program to find longest common
# subarray of two binary arrays with
# same sum

def longestCommonSum(arr1, arr2, n):

	# Initialize result
	maxLen = 0
	
	# Initialize prefix sums of two arrays
	presum1 = presum2 = 0
	
	# Create a dictionary to store indices
	# of all possible sums
	diff = {}
	
	# Traverse both arrays
	for i in range(n):
	
		# Update prefix sums
		presum1 += arr1[i]
		presum2 += arr2[i]
		
		# Compute current diff which will be
		# used as index in diff dictionary
		curr_diff = presum1 - presum2
		
		# If current diff is 0, then there
		# are same number of 1's so far in
		# both arrays, i.e., (i+1) is
		# maximum length.
		if curr_diff == 0:
			maxLen = i+1
		elif curr_diff not in diff:
			# save the index for this diff
			diff[curr_diff] = i
		else:				
			# calculate the span length
			length = i - diff[curr_diff]
			maxLen = max(maxLen, length)
		
	return maxLen

# Driver program
arr1 = [0, 1, 0, 1, 1, 1, 1]
arr2 = [1, 1, 1, 1, 1, 0, 1]
print("Length of the longest common",
	" span with same", end = " ")
print("sum is",longestCommonSum(arr1,
				arr2, len(arr1)))

# This code is contributed by Abhijeet Nautiyal
