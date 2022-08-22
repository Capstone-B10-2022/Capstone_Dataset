# Python3 program to Rearrange positive
# and negative numbers in an array

# Function to print an array


def printArray(A, size):

	for i in range(0, size):
		print(A[i], end=" ")
	print()

# Function to reverse an array. An array can
# be reversed in O(n) time and O(1) space.


def reverse(arr, l, r):

	if l < r:

		arr[l], arr[r] = arr[r], arr[l]
		l, r = l + 1, r - 1
		reverse(arr, l, r)

# Merges two subarrays of arr[].
# First subarray is arr[l..m]
# Second subarray is arr[m + 1..r]


def merge(arr, l, m, r):

	i = l # Initial index of 1st subarray
	j = m + 1 # Initial index of IInd

	while i <= m and arr[i] < 0:
		i += 1

	# arr[i..m] is positive

	while j <= r and arr[j] < 0:
		j += 1

	# arr[j..r] is positive

	# reverse positive part of left
	# sub-array (arr[i..m])
	reverse(arr, i, m)

	# reverse negative part of right
	# sub-array (arr[m + 1..j-1])
	reverse(arr, m + 1, j - 1)

	# reverse arr[i..j-1]
	reverse(arr, i, j - 1)

# Function to Rearrange positive
# and negative numbers in a array


def RearrangePosNeg(arr, l, r):

	if l < r:

		# Same as (l + r)/2, but avoids
		# overflow for large l and h
		m = l + (r - l) // 2

		# Sort first and second halves
		RearrangePosNeg(arr, l, m)
		RearrangePosNeg(arr, m + 1, r)

		merge(arr, l, m, r)


# Driver Code
if __name__ == "__main__":

	arr = [-12, 11, -13, -5, 6, -7, 5, -3, -6]
	arr_size = len(arr)

	RearrangePosNeg(arr, 0, arr_size - 1)

	printArray(arr, arr_size)

# This code is contributed by Rituraj Jain
