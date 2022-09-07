# Python Program Illustrating Naive Approach to
# Find if There is a Pair in A[0..N-1] with Given Sum
#https://www.geeksforgeeks.org/two-pointers-technique/
# Method


def isPairSum(A, N, X):

	for i in range(N):
		for j in range(N):

			# as equal i and j means same element
			if(i == j):
				continue

			# pair exists
			if (A[i] + A[j] == X):
				return True

			# as the array is sorted
			if (A[i] + A[j] > X):
				break

	# No pair found with given sum
	return 0


# Driver code
arr = [2, 3, 5, 8, 9, 10, 11]
val = 17

print(isPairSum(arr, len(arr), val))

# This code is contributed by maheshwaripiyush9
