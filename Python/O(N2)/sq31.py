# Python 3 for printing smallest
# k numbers in order

# Function to print smallest k
# numbers in arr[0..n-1]


def printSmall(arr, n, k):

	# For each arr[i] find whether
	# it is a part of n-smallest
	# with insertion sort concept
	for i in range(k, n):

		# find largest from first k-elements
		max_var = arr[k - 1]
		pos = k - 1
		for j in range(k - 2, -1, -1):

			if (arr[j] > max_var):

				max_var = arr[j]
				pos = j

		# if largest is greater than arr[i]
		# shift all element one place left
		if (max_var > arr[i]):

			j = pos
			while (j < k - 1):

				arr[j] = arr[j + 1]
				j += 1

			# make arr[k-1] = arr[i]
			arr[k - 1] = arr[i]

	# print result
	for i in range(0, k):
		print(arr[i], end=" ")


# Driver program
arr = [1, 5, 8, 9, 6, 7, 3, 4, 2, 0]
n = len(arr)
k = 5
printSmall(arr, n, k)
