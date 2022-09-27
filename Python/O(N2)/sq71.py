# Python3 program to Find the two
# repeating elements in a given array
#https://www.geeksforgeeks.org/find-the-two-repeating-elements-in-a-given-array/
def printRepeating(arr, size):

	print("Repeating elements are ",
						end = '')
	for i in range (0, size-1):
		for j in range (i + 1, size):
			if arr[i] == arr[j]:
				print(arr[i], end = ' ')
	
# Driver code
arr = [4, 2, 4, 5, 2, 3, 1]
arr_size = len(arr)
printRepeating(arr, arr_size)

# This code is contributed by Smitha Dinesh Semwal
