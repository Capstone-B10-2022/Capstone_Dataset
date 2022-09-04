# Source: https://www.geeksforgeeks.org/number-subarrays-given-product/

# Python3 program to find number of subarrays
# having product exactly equal to k.

# Function to find number of subarrays
# having product equal to 1.
def countOne(arr, n) :
	i = 0
	
	# To store number of ones in
	# current segment of all 1s.
	Len = 0
	
	# To store number of subarrays
	# having product equal to 1.
	ans = 0
	
	while(i < n) :
		
		# If current element is 1, then
		# find length of segment of 1s
		# starting from current element.
		if(arr[i] == 1) :
			Len = 0
			while(i < n and arr[i] == 1) :
				i += 1
				Len += 1
			
			# add number of possible
			# subarrays of 1 to result.
			ans += (Len*(Len+1)) // 2
		i += 1
	
	return ans

# Function to find number of subarrays having
# product exactly equal to k.
def findSubarrayCount(arr, n, k) :

	start, endval, p, countOnes, res = 0, 0, 1, 0, 0

	while (endval < n) :
	
		p = p * (arr[endval])

		# If product is greater than k then we need to decrease
		# it. This could be done by shifting starting point of
		# sliding window one place to right at a time and update
		# product accordingly.
		if(p > k) :
		
			while(start <= endval and p > k) :
			
				p = p // arr[start]
				start += 1
				
		if(p == k) :
		
			# Count number of succeeding ones.
			countOnes = 0
			while endval + 1 < n and arr[endval + 1] == 1 :
			
				countOnes += 1
				endval += 1

			# Update result by adding both new subarray
			# and effect of succeeding ones.
			res += (countOnes + 1)

			# Update sliding window and result according
			# to change in sliding window. Here preceding
			# 1s have same effect on subarray as succeeding
			# 1s, so simply add.
			while(start <= endval and arr[start] == 1 and k!=1) :
			
				res += (countOnes + 1)
				start += 1

			# Move start to correct position to find new
			# subarray and update product accordingly.
			p = p // arr[start]
			start += 1

		endval += 1

	return res

arr1 = [ 2, 1, 1, 1, 3, 1, 1, 4 ]
n1 = len(arr1)
k = 1

if(k != 1) :
	print(findSubarrayCount(arr1, n1, k))
else :
	print(countOne(arr1, n1))

arr2 = [ 2, 1, 1, 1, 4, 5]
n2 = len(arr2)
k = 4

if(k != 1) :
	print(findSubarrayCount(arr2, n2, k))
else :
	print(countOne(arr2, n2))

	# This code is contributed by divyesh072019
