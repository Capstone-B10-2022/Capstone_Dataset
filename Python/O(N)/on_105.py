# Source: https://www.geeksforgeeks.org/sort-array-contain-1-n-values/

# Python3 program to sort an array of
# numbers in range from 1 to n.

# function for sort array
def sortit(arr,n):
	for i in range(n):
		arr[i] = i+1

# Driver code
if __name__=='__main__':
	arr = [10, 7, 9, 2, 8, 3, 5, 4, 6, 1 ]
	n = len(arr)

	# for sort an array
	sortit(arr,n)

	# for print all the element
	# in sorted way
	for i in range(n):
		print(arr[i],end=" ")

# This code is contributed by
# Shrikant13
