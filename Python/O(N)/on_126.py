# Source: https://www.geeksforgeeks.org/find-repetitive-element-1-n-1/

# Python3 program to find the only
# repeating element in an array
# where elements are from 1 to n-1.


def findRepeating(arr, N):
	s = set()
	for i in range(N):
		if arr[i] in s:
			return arr[i]
		s.add(arr[i])

	# If input is correct, we should
	# never reach here
	return -1


# Driver code
if __name__ == "__main__":
arr = [9, 8, 2, 6, 1, 8, 5, 3]
N = len(arr)

# Function call
print(findRepeating(arr, N))

# This code is contributed
# by Shrikant13
