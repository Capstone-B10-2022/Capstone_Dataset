# Source: https://www.geeksforgeeks.org/shortest-un-ordered-subarray/

# Python3 program to find shortest
# subarray which is unsorted

# Bool function for checking an array
# elements are in increasing
def increasing(a, n):

	for i in range(0, n - 1):
		if (a[i] >= a[i + 1]):
			return False
			
	return True

# Bool function for checking an array
# elements are in decreasing
def decreasing(a, n):

	for i in range(0, n - 1):
		if (a[i] < a[i + 1]):
			return False
			
	return True

def shortestUnsorted(a, n):

	# increasing and decreasing are two functions.
	# if function return True value then print
	# 0 otherwise 3.
	if (increasing(a, n) == True or
		decreasing(a, n) == True):
		return 0
	else:
		return 3

# Driver code
ar = [7, 9, 10, 8, 11]
n = len(ar)
print(shortestUnsorted(ar, n))

# This code is contributed by Smitha Dinesh Semwal.
