# Python 3 program to Rearrange positive
# and negative numbers in a array

# A utility function to print
# an array of size n


def printArray(arr, n):
	for i in range(n):
		print(arr[i], end=" ")
	print()

# Function to Rearrange positive
# and negative numbers in a array


def RearrangePosNeg(arr, n):

	for i in range(1, n):
		key = arr[i]

		# if current element is positive
		# do nothing
		if (key > 0):
			continue

		
		j = i - 1
		while (j >= 0 and arr[j] > 0):
			arr[j + 1] = arr[j]
			j = j - 1

		# Put negative element at its
		# right position
		arr[j + 1] = key


# Driver Code
if __name__ == "__main__":
	arr = [-12, 11, -13, -5,
		6, -7, 5, -3, -6]
	n = len(arr)

	RearrangePosNeg(arr, n)
	printArray(arr, n)

# This code is contributed
# by ChitraNayal
