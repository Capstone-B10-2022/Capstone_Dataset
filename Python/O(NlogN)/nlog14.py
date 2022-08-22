# Sorting based Python 3 program
# to find all elements in array
# which have atleast two greater
# elements itself.

def findElements(arr, n):

	arr.sort()

	for i in range(0, n-2):
		print(arr[i], end =" ")

# Driven source
arr = [2, -6, 3, 5, 1]
n = len(arr)
findElements(arr, n)

# This code is contributed
# by Smitha Dinesh Semwal
