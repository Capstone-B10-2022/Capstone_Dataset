# Source: https://www.geeksforgeeks.org/sort-array-containing-two-types-elements/

# Python3 program to sort an array with
# two types of values in one traversal.

# Method for segregation 0 and
# 1 given input array
def segregate0and1(arr, n):

	type0 = 0; type1 = n - 1

	while (type0 < type1):
		if (arr[type0] == 1):
			arr[type0], arr[type1] = arr[type1], arr[type0]
			type1 -= 1
		
		else:
			type0 += 1
		
# Driver Code
arr = [1, 1, 1, 0, 1, 0, 0, 1, 1, 1, 1]
n = len(arr)
segregate0and1(arr, n)
for i in range(0, n):
	print(arr[i], end = " ")

# This code is contributed by Smitha Dinesh Semwal
