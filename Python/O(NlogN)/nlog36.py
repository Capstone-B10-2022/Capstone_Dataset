# Python3 implementation using STL
#https://www.geeksforgeeks.org/two-elements-whose-sum-is-closest-to-zero/
import sys

def findMinSum(arr, n):
	
	for i in range(1, n):
		
		# Modified to sort by absolute values
		if (not abs(arr[i - 1]) < abs(arr[i])):
			arr[i - 1], arr[i] = arr[i], arr[i - 1]

	Min = sys.maxsize
	x = 0
	y = 0

	for i in range(1, n):
		
		# Absolute value shows how
		# close it is to zero
		if (abs(arr[i - 1] + arr[i]) <= Min):
			
			# If found an even close value
			# update min and store the index
			Min = abs(arr[i - 1] + arr[i])
			x = i - 1
			y = i

	print("The two elements whose sum is minimum are",
		arr[x], "and", arr[y])

# Driver code
arr = [ 1, 60, -10, 70, -80, 85 ]
n = len(arr)

findMinSum(arr, n)

# This code is contributed by avanitrachhadiya2155
