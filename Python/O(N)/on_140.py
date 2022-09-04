# Source: https://www.geeksforgeeks.org/find-a-fixed-point-in-a-given-array/

# Python program to check fixed point
# in an array using linear search
def linearSearch(arr, n):
	for i in range(n):
		if arr[i] is i:
			return i
	# If no fixed point present then return -1
	return -1

# Driver program to check above functions
arr = [-10, -1, 0, 3, 10, 11, 30, 50, 100]
n = len(arr)
print("Fixed Point is " + str(linearSearch(arr, n)))

# This code is contributed by Pratik Chhajer
