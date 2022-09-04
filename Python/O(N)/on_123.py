# Source: https://www.geeksforgeeks.org/find-repetitive-element-1-n-1/

# Python3 program to find the only
# repeating element in an array
# where elements are from 1 to N-1.

# Function to find repeated element


def findRepeating(arr, N):

	missingElement = 0

	# indexing based
	for i in range(0, N):

		element = arr[abs(arr[i])]

		if(element < 0):
			missingElement = arr[i]
			break

		arr[abs(arr[i])] = -arr[abs(arr[i])]

	return abs(missingElement)


# Driver code
if __name__ == "__main__":
arr = [9, 8, 2, 6, 1, 8, 5, 3, 4, 7]
N = len(arr)

# Function call
print(findRepeating(arr, N))

# This code is contributed by Smitha Dinesh Semwal.
