# Source: https://www.geeksforgeeks.org/find-the-two-repeating-elements-in-a-given-array/

# Python3 program to find the two repeating
# elements in a given array
def printRepeating(arr, size):
	
	s = set()
	print("The two Repeating elements are : ", end = "")
	
	for i in range(size):
		if (len(s) and arr[i] in s):
			print(arr[i], end = " ")
			
		s.add(arr[i])
		
# Driver code
arr = [ 4, 2, 4, 5, 2, 3, 1 ]
arr_size = len(arr)
printRepeating(arr, arr_size)

# This code is contributed by Shubham Singh
