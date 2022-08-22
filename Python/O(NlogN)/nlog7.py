# Python3 program to Rearrange positive
# and negative numbers in a array

# Function to print an array


def printArray(A, size):

	for i in range(size):
		print(A[i], end=" ")
	print()

# Merges two subarrays of arr[].
# First subarray is arr[l..m]
# Second subarray is arr[m + 1..r]


def merge(arr, l, m, r):
	i, j, k = 0, 0, 0
	n1 = m - l + 1
	n2 = r - m

	# create temp arrays */
	L = [arr[l + i] for i in range(n1)]
	R = [arr[m + 1 + j] for j in range(n2)]

	# Merge the temp arrays back into arr[l..r]*/
	i = 0 # Initial index of first subarray
	j = 0 # Initial index of second subarray
	k = l # Initial index of merged subarray

	# Note the order of appearance of elements
	# should be maintained - we copy elements
	# of left subarray first followed by that
	# of right subarray

	# copy negative elements of left subarray
	while (i < n1 and L[i] < 0):
		arr[k] = L[i]
		k += 1
		i += 1

	# copy negative elements of right subarray
	while (j < n2 and R[j] < 0):
		arr[k] = R[j]
		k += 1
		j += 1

	# copy positive elements of left subarray
	while (i < n1):
		arr[k] = L[i]
		k += 1
		i += 1

	# copy positive elements of right subarray
	while (j < n2):
		arr[k] = R[j]
		k += 1
		j += 1

# Function to Rearrange positive and
# negative numbers in a array


def RearrangePosNeg(arr, l, r):

	if(l < r):

		# Same as (l + r)/2, but avoids
		# overflow for large l and h
		m = l + (r - l) // 2

		# Sort first and second halves
		RearrangePosNeg(arr, l, m)
		RearrangePosNeg(arr, m + 1, r)

		merge(arr, l, m, r)


# Driver Code
arr = [-12, 11, -13, -5,
	6, -7, 5, -3, -6]
arr_size = len(arr)

RearrangePosNeg(arr, 0, arr_size - 1)

printArray(arr, arr_size)

# This code is contributed by
# mohit kumar 29
