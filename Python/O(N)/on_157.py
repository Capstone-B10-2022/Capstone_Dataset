# Source: https://www.geeksforgeeks.org/check-if-array-elements-are-consecutive/

# Helper functions to get Minimum and
# Maximum in an array

# The function checks if the array elements
# are consecutive. If elements are consecutive,
# then returns true, else returns false
def areConsecutive(arr, n):

	if ( n < 1 ):
		return False
	
	# 1) Get the Minimum element in array */
	Min = min(arr)
	
	# 2) Get the Maximum element in array */
	Max = max(arr)
	
	# 3) Max - Min + 1 is equal to n,
	# then only check all elements */
	if (Max - Min + 1 == n):
		
		# Create a temp array to hold visited
		# flag of all elements. Note that, calloc
		# is used here so that all values are
		# initialized as false
		visited = [False for i in range(n)]
	
		for i in range(n):
			
			# If we see an element again,
			# then return false */
			if (visited[arr[i] - Min] != False):
				return False
	
			# If visited first time, then mark
			# the element as visited */
			visited[arr[i] - Min] = True
	
		# If all elements occur once,
		# then return true */
		return True
	
	return False # if (Max - Min + 1 != n)

# Driver Code
arr = [5, 4, 2, 3, 1, 6]
n = len(arr)
if(areConsecutive(arr, n) == True):
	print("Array elements are consecutive ")
else:
	print("Array elements are not consecutive ")

# This code is contributed by mohit kumar
