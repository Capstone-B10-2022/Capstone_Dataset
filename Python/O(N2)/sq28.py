import heapq


def kthSmallest(matrix, k):
	# n = size of matrix
	n = len(matrix)

	# using built-in priority queue which acts as max Heap i.e. largest element will be on top
	# Kth smallest element can also be seen as largest element in a priority queue of size k
	# By this logic we pop elements from priority queue when its size becomes greater than k
	# thus top of priority queue is kth smallest element in matrix

	maxH = []
	for i in range(n):
		for j in range(n):
			heapq.heappush(maxH, -matrix[i][j])
			if len(maxH) > k:
				heapq.heappop(maxH)
	return -maxH[0]


matrix = [[1, 5, 9], [10, 11, 13], [12, 13, 15]]
k = 8
print("8th smallest element is", kthSmallest(matrix, k))

# This code is comtributed by Tapesh (tapeshdua420)
