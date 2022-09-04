# Source: https://www.geeksforgeeks.org/find-repetitive-element-1-n-1/

# Python3 program to find the only
# repeating element in an array where
# elements are from 1 to N-1.


def findRepeating(arr, N):

	# res is going to store value of
	# 1 ^ 2 ^ 3 .. ^ (N-1) ^ arr[0] ^
	# arr[1] ^ .... arr[n-1]
	res = 0
	for i in range(0, N-1):
		res = res ^ (i+1) ^ arr[i]
	res = res ^ arr[N-1]

	return res


# Driver code
if __name__ == "__main__":
arr = [9, 8, 2, 6, 1, 8, 5, 3, 4, 7]
N = len(arr)

# Function call
print(findRepeating(arr, N))

# This code is contributed by Smitha Dinesh Semwal.
