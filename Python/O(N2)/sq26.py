# Python3 code for the above approach

# This function returns k'th smallest element
# in arr[l..r] using QuickSort based method.
# ASSUMPTION: ALL ELEMENTS IN ARR[] ARE DISTINCT
import sys


def kthSmallest(arr, l, r, K):

	# If k is smaller than number of
	# elements in array
	if (K > 0 and K <= r - l + 1):

		# Partition the array around last
		# element and get position of pivot
		# element in sorted array
		pos = partition(arr, l, r)

		# If position is same as k
		if (pos - l == K - 1):
			return arr[pos]
		if (pos - l > K - 1): # If position is more,
							# recur for left subarray
			return kthSmallest(arr, l, pos - 1, K)

		# Else recur for right subarray
		return kthSmallest(arr, pos + 1, r,
						K - pos + l - 1)

	# If k is more than number of
	# elements in array
	return sys.maxsize

# Standard partition process of QuickSort().
# It considers the last element as pivot and
# moves all smaller element to left of it
# and greater elements to right


def partition(arr, l, r):

	x = arr[r]
	i = l
	for j in range(l, r):
		if (arr[j] <= x):
			arr[i], arr[j] = arr[j], arr[i]
			i += 1
	arr[i], arr[r] = arr[r], arr[i]
	return i


# Driver's Code
if __name__ == "__main__":

	arr = [12, 3, 5, 7, 4, 19, 26]
	N = len(arr)
	K = 3
	print("K'th smallest element is",
		kthSmallest(arr, 0, N - 1, K))

# This code is contributed by ita_c
