# Binary Search based Python3
# program to find number of
# rotations in a sorted and
# rotated array.

#https://www.geeksforgeeks.org/find-rotation-count-rotated-sorted-array/
# Returns count of rotations for
# an array which is first sorted
# in ascending order, then rotated

def countRotations(arr, n):
	start = 0
	end = n-1

	# Finding the index of minimum of the array
	# index of min would be equal to number to rotation
	while start<=end:
		mid = start+(end-start)//2
		
		# Calculating the previous(prev)
		# and next(nex) index of mid
		prev = (mid-1+n)%n
		nex = (mid+1)%n

		# Checking if mid is minimum
		if arr[mid]<arr[prev]\
		and arr[mid]<=arr[nex]:
		return mid
	
		# if not selecting the unsorted part of array
		elif arr[mid]<arr[start]: end = mid-1
		elif arr[mid]>arr[end]: start = mid+1
		else: return 0

# Driver code
if __name__ == '__main__':
	arr = [15, 18, 2, 3, 6, 12]
	N = len(arr)
	print(countRotations(arr, N))

# This code is contributed by Smitha Dinesh Semwal
