# Source: https://www.geeksforgeeks.org/search-insert-and-delete-in-an-unsorted-array/

# Python program for searching in
# unsorted array


def findElement(arr, n, key):
	for i in range(n):
		if (arr[i] == key):
			return i
		
	# If the key is not found
	return -1


# Driver's code
if __name__ == '__main__':
	arr = [12, 34, 10, 6, 40]
	key = 40
	n = len(arr)

	# search operation
	index = findElement(arr, n, key)
	if index != -1:
		print("Element Found at position: " + str(index + 1))
	else:
		print("Element not found")

	# Thanks to Aditi Sharma for contributing
	# this code
