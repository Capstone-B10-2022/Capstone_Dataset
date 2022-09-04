# Source: https://www.geeksforgeeks.org/search-insert-and-delete-in-an-unsorted-array/

# Python program to delete an element
# from an unsorted array

# Driver's code
if __name__ == '__main__':
	# Declaring array and key to delete
	arr = [10, 50, 30, 40, 20]
	key = 30

	print("Array before deletion:")
	print (arr)

	# deletes key if found in the array
	# otherwise shows error not in list
	arr.remove(key)
	print("Array after deletion")
	print(arr)

	# This code is contributed by Aditi Sharma.
