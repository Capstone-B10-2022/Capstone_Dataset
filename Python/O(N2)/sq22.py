# A O(n) time and O(1) extra space C++ program to
# sort an array according to given indexes
def swap(arr, i, j):
	temp = arr[i]
	arr[i] = arr[j]
	arr[j] = temp

# Function to reorder elements of arr[] according
# to index[]
def reorder(arr, index_arr, n):

# Fix all elements one by one
	for i in range(n):
	
	# While index[i] and arr[i] are not fixed
		while index_arr[i] != i:
			swap(arr, i, index_arr[i])
			swap(index_arr, i, index_arr[i])

# Driver program
if __name__ == "__main__":
	arr = [50, 40, 70, 60, 90]
	index = [3, 0, 4, 1, 2]
	n = len(arr)
	reorder(arr, index, n)
	print("Reordered array is: ")
	for i in range(n):
		print(arr[i], end=" ")
	print("\nModified Index array is: ")
	for i in range(n):
		print(index[i], end=" ")

# This code is contributed by Tapesh(tapeshdua420)
