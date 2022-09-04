# Source: https://www.geeksforgeeks.org/given-an-array-a-and-a-number-x-check-for-pair-in-a-with-sum-as-x/

# Python program to find if there are
# two elements with given sum

# function to check for the given sum
# in the array
def printPairs(arr, arr_size, sum):
	
	# Create an empty hash map
	# using an hashmap allows us to store the indices
	hashmap = {}
	
	for i in range(0, arr_size):
		temp = sum-arr[i]
		if (temp in hashmap):
			print (f'Pair with given sum {sum} is ({temp},{arr[i]}) at indices ({hashmap[temp]},{i})')
		hashmap[arr[i]] = i

# driver code
A = [1, 4, 45, 6, 10, 8]
n = 16
printPairs(A, len(A), n)

# This code will also work in case the array has the same number twice
# and target is the sum of those numbers
# Eg: Array = [4,6,4] Target = 8

# This code is contributed by __Achyut Upadhyay__
