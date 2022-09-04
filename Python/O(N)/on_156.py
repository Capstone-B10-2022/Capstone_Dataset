# Source: https://www.geeksforgeeks.org/check-if-array-elements-are-consecutive/

# Helper functions to get minimum and
# maximum in an array

# The function checks if the array
# elements are consecutive. If elements
# are consecutive, then returns true,
# else returns false
def areConsecutive(arr, n):

	if ( n < 1 ):
		return False

	# 1) Get the minimum element in array
	min = getMin(arr, n)

	# 2) Get the maximum element in array
	max = getMax(arr, n)

	# 3) max - min + 1 is equal to n
	# then only check all elements
	if (max - min + 1 == n):

		for i in range(n):

			if (arr[i] < 0):
				j = -arr[i] - min
			else:
				j = arr[i] - min

			# if the value at index j is negative
			# then there is repetition
			if (arr[j] > 0):
				arr[j] = -arr[j]
			else:
				return False

		# If we do not see a negative value
		# then all elements are distinct
		return True

	return False	 # if (max - min + 1 != n)

# UTILITY FUNCTIONS
def getMin(arr, n):
	
	min = arr[0]
	for i in range(1, n):
		if (arr[i] < min):
			min = arr[i]
	return min

def getMax(arr, n):
	max = arr[0]
	for i in range(1, n):
		if (arr[i] > max):
			max = arr[i]
	return max

# Driver Code
if __name__ == "__main__":
	
	arr = [1, 4, 5, 3, 2, 6]
	n = len(arr)
	if(areConsecutive(arr, n) == True):
		print(" Array elements are consecutive ")
	else:
		print(" Array elements are not consecutive ")

# This code is contributed by ita_c
