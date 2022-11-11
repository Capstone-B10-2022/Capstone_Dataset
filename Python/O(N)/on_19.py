# Python program to find minimum element
# in a sorted and rotated array
#https://www.geeksforgeeks.org/find-minimum-element-in-a-sorted-and-rotated-array/
 
# python3 code to implement the approach

def findMin(arr, N):
	
	min_ele = arr[0];

	# Traversing over array to
	# find minimum element
	for i in range(N) :
		if arr[i] < min_ele :
			min_ele = arr[i]

	return min_ele;

# Driver program
arr = [5, 6, 1, 2, 3, 4]
N = len(arr)

print(findMin(arr,N))

# This code is contributed by aditya942003patil
