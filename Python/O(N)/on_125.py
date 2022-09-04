# Source: https://www.geeksforgeeks.org/find-repetitive-element-1-n-1/

# Python3 program to find the only
# repeating element in an array where
# elements are from 1 to N-1.


def findRepeating(arr, N):

	# Find array sum and subtract sum
	# first n-1 natural numbers from it
	# to find the result.
	return sum(arr) - (((N - 1) * N) // 2)


# Driver's Code
if __name__ == "__main__":
arr = [9, 8, 2, 6, 1, 8, 5, 3, 4, 7]
N = len(arr)

# Function call
print(findRepeating(arr, N))

# This code is contributed
# by mohit kumar
