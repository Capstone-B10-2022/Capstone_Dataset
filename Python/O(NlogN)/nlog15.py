# This returns count of elements in matrix
# less than of equal to num
def getElementsGreaterThanOrEqual(num,n,mat):
	ans = 0
	for i in range(n):
	
		# if num is less than the first element
		# then no more element in matrix
		# further are less than or equal to num
		if (mat[i][0] > num):
			return ans
		
		# if num is greater than last element,
		# it is greater than all elements
		# in that row
		if (mat[i][n - 1] <= num):
			ans += n
			continue
		# This contain the col index of last element
		# in matrix less than of equal
		# to num
		greaterThan = 0
		jump = n // 2
		while(jump >= 1):
				while (greaterThan + jump < n and mat[i][greaterThan + jump] <= num):
					greaterThan += jump
				jump //= 2

		ans += greaterThan + 1
	return ans

# returns kth smallest index in the matrix
def kthSmallest(mat, n, k):

	# We know the answer lies between
	# the first and the last element
	# So do a binary search on answer
	# based on the number of elements
	# our current element is greater than
	# the elements in the matrix
	l,r = mat[0][0],mat[n - 1][n - 1]

	while (l <= r):
		mid = l + (r - l) // 2
		greaterThanOrEqualMid = getElementsGreaterThanOrEqual(mid, n, mat)

		if (greaterThanOrEqualMid >= k):
			r = mid - 1
		else:
			l = mid + 1

	return l

# driver code
n = 4
mat = [[10, 20, 30, 40],[15, 25, 35, 45],[25, 29, 37, 48],[32, 33, 39, 50]]
print(f"7th smallest element is {kthSmallest(mat, 4, 7)}")

# This code is contributed by shinjanpatra
#ynlogn