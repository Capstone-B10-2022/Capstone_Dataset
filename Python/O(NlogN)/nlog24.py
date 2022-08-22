# Python3 program to find
# k-th absolute difference
# between two elements
from bisect import bisect as upper_bound

# returns number of pairs with
# absolute difference less than
# or equal to mid.
def countPairs(a, n, mid):
	res = 0
	for i in range(n):

		# Upper bound returns pointer to position
		# of next higher number than a[i]+mid in
		# a[i..n-1]. We subtract (a + i + 1) from
		# this position to count
		res += upper_bound(a, a[i] + mid)
	return res

# Returns k-th absolute difference
def kthDiff(a, n, k):
	
	# Sort array
	a = sorted(a)

	# Minimum absolute difference
	low = a[1] - a[0]
	for i in range(1, n - 1):
		low = min(low, a[i + 1] - a[i])

	# Maximum absolute difference
	high = a[n - 1] - a[0]

	# Do binary search for k-th absolute difference
	while (low < high):
		mid = (low + high) >> 1
		if (countPairs(a, n, mid) < k):
			low = mid + 1
		else:
			high = mid

	return low

# Driver code
k = 3
a = [1, 2, 3, 4]
n = len(a)
print(kthDiff(a, n, k))

# This code is contributed by Mohit Kumar
