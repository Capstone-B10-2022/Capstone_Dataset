# Source: https://www.geeksforgeeks.org/longest-span-sum-two-binary-arrays/
# Python program to find largest subarray
# with equal number of 0's and 1's.

# Returns largest common subarray with equal
# number of 0s and 1s
def longestCommonSum(arr1, arr2, n):
	
	# Find difference between the two
	arr = [0 for i in range(n)]
	
	for i in range(n):
		arr[i] = arr1[i] - arr2[i];
	
	# Creates an empty hashMap hM
	hm = {}
	sum = 0	 # Initialize sum of elements
	max_len = 0	 #Initialize result
	
	# Traverse through the given array
	for i in range(n):
		
		# Add current element to sum
		sum += arr[i]
		
		# To handle sum=0 at last index
		if (sum == 0):
			max_len = i + 1
		
		# If this sum is seen before,
		# then update max_len if required
		if sum in hm:
			max_len = max(max_len, i - hm[sum])
		else: # Else put this sum in hash table
			hm[sum] = i
	return max_len

# Driver code
arr1 = [0, 1, 0, 1, 1, 1, 1]
arr2 = [1, 1, 1, 1, 1, 0, 1]
n = len(arr1)
print(longestCommonSum(arr1, arr2, n))

# This code is contributed by rag2127
