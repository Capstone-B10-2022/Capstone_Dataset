# Python3 program for above approach

#https://www.geeksforgeeks.org/find-the-first-missing-number/
# Function to find Smallest
# Missing in Sorted Array
def findSmallestMissinginSortedArray(arr):
	
	# Check if 0 is missing
	# in the array
	if (arr[0] != 0):
		return 0
	
	# Check is all numbers 0 to n - 1
	# are present in array
	if (arr[-1] == len(arr) - 1):
		return len(arr)
	
	first = arr[0]
	
	return findFirstMissing(arr, 0,
			len(arr) - 1, first)

# Function to find missing element
def findFirstMissing(arr, start, end, first):
	
	if (start < end):
		mid = int((start + end) / 2)
		
		# Index matches with value
		# at that index, means missing
		# element cannot be upto that point
		if (arr[mid] != mid + first):
			return findFirstMissing(arr, start,
									mid, first)
		else:
			return findFirstMissing(arr, mid + 1,
									end, first)
	
	return start + first

# Driver code
arr = [ 0, 1, 2, 3, 4, 5, 7 ]
n = len(arr)

# Function Call
print("First Missing element is :",
	findSmallestMissinginSortedArray(arr))

# This code is contributed by rag2127
