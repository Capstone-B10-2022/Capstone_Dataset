# Python3 code to rearrange the array
# as per the given condition
import array as a
import numpy as np

# function to rearrange the array
def rearrangeArr(arr, n):
	
	# total even positions
	evenPos = int(n / 2)

	# total odd positions
	oddPos = n - evenPos

	# initialising empty array in python
	tempArr = np.empty(n, dtype = object)

	# copy original array in an
	# auxiliary array
	for i in range(0, n):
		
		tempArr[i] = arr[i]

	# sort the auxiliary array
	tempArr.sort()

	j = oddPos - 1

	# fill up odd position in original
	# array
	for i in range(0, n, 2):

		arr[i] = tempArr[j]
		j = j - 1
	
	j = oddPos

	# fill up even positions in original
	# array
	for i in range(1, n, 2):
		arr[i] = tempArr[j]
		j = j + 1
	
	# display array
	for i in range(0, n):
		print (arr[i], end = ' ')

# Driver code
arr = a.array('i', [ 1, 2, 3, 4, 5, 6, 7 ])
rearrangeArr(arr, 7)

# This code is contributed by saloni1297
