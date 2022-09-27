# Python program to find
# K maximum combinations
# from two arrays
import math
from queue import PriorityQueue

# Function to display first K
# maximum sum combinations


def KMaxCombinations(A, B, N, K):

	# Max heap.
	pq = PriorityQueue()

	# Insert all the possible
	# combinations in max heap.
	for i in range(0, N):
		for j in range(0, N):
			a = A[i] + B[j]
			pq.put((-a, a))

	# Pop first N elements from
	# max heap and display them.
	count = 0
	while (count < K):
		print(pq.get()[1])
		count = count + 1


# Driver method
A = [4, 2, 5, 1]
B = [8, 0, 5, 3]
N = len(A)
K = 3

# Function call
KMaxCombinations(A, B, N, K)

# This code is contributed
# by Gitanjali.
