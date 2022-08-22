# Program for kth largest element in a 2d array
# sorted row-wise and column-wise
from sys import maxsize

# A structure to store an entry of heap.
# The entry contains a value from 2D array,
# row and column numbers of the value
class HeapNode:
	def __init__(self, val, r, c):
		self.val = val # value to be stored
		self.r = r # Row number of value in 2D array
		self.c = c # Column number of value in 2D array

# A utility function to minheapify the node harr[i]
# of a heap stored in harr[]
def minHeapify(harr, i, heap_size):
	l = i * 2 + 1
	r = i * 2 + 2
	if(l < heap_size and r<heap_size and harr[l].val < harr[i].val and harr[r].val < harr[i].val):
	temp= HeapNode(0,0,0)
	temp=harr[r]
	harr[r]=harr[i]
	harr[i]=harr[l]
	harr[l]=temp
	minHeapify(harr ,l,heap_size)
	minHeapify(harr ,r,heap_size)
	if (l < heap_size and harr[l].val < harr[i].val):
	temp= HeapNode(0,0,0)
	temp=harr[i]
	harr[i]=harr[l]
	harr[l]=temp
	minHeapify(harr ,l,heap_size)
			
# This function returns kth smallest element
# in a 2D array mat[][]
def kthSmallest(mat, n, k):

	# k must be greater than 0 and smaller than n*n
	if k < 0 or k > n * n:
		return maxsize

	# Create a min heap of elements from
	# first row of 2D array
	harr = [0] * n
	for i in range(n):
		harr[i] = HeapNode(mat[0][i], 0, i)

	hr = HeapNode(0, 0, 0)
	for i in range(k):

		# Get current heap root
		hr = harr[0]

		# Get next value from column of root's value.
		# If the value stored at root was last value
		# in its column, then assign INFINITE as next value
		nextval = mat[hr.r + 1][hr.c] if (hr.r < n - 1) else maxsize

		# Update heap root with next value
		harr[0] = HeapNode(nextval, hr.r + 1, hr.c)

		# Heapify root
		minHeapify(harr, 0, n)

	# Return the value at last extracted root
	return hr.val

# Driver Code
if __name__ == "__main__":
	mat = [[10, 20, 30, 40],
		[15, 25, 35, 45],
		[25, 29, 37, 48],
		[32, 33, 39, 50]]
	print("7th smallest element is",
			kthSmallest(mat, 4, 7))

# This code is contributed by Rishabh Chauhan
