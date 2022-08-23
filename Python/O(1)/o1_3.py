# Python3 program for the above approach
#https://www.geeksforgeeks.org/python3-program-to-find-the-mth-element-of-the-array-after-k-left-rotations/
# Function to return Mth element of
# array after k left rotations
def getFirstElement(a, N, K, M):
	
	# The array comes to original state
	# after N rotations
	K %= N

	# Mth element after k left rotations
	# is (K+M-1)%N th element of the
	# original array
	index = (K + M - 1) % N

	result = a[index]

	# Return the result
	return result

# Driver Code
if __name__ == '__main__':
	
	# Array initialization
	a = [ 3, 4, 5, 23 ]

	# Size of the array
	N = len(a)

	# Given K rotation and Mth element
	# to be found after K rotation
	K = 2
	M = 1

	# Function call
	print(getFirstElement(a, N, K, M))

# This code is contributed by mohit kumar 29
