# Source: https://www.geeksforgeeks.org/searching-array-adjacent-differ-k/

# Python 3 program to search an element in an array
# where difference between adjacent elements is atmost k

# x is the element to be searched in arr[0..n-1]
# such that all elements differ by at-most k.
def search(arr, n, x, k):

	# Traverse the given array starting from
	# leftmost element
	i = 0
	while (i < n):
	
		# If x is found at index i
		if (arr[i] == x):
			return i

		# Jump the difference between current
		# array element and x divided by k
		# We use max here to make sure that i
		# moves at-least one step ahead.
		i = i + max(1, int(abs(arr[i] - x) / k))
	

	print("number is not present!")
	return -1


# Driver program to test above function
arr = [2, 4, 5, 7, 7, 6]
x = 6
k = 2
n = len(arr)
print("Element", x, "is present at index",search(arr, n, x, k))

# This code is contributed
# by Smitha Dinesh Semwal
