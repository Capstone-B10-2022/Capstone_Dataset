#https://www.geeksforgeeks.org/count-number-of-occurrences-or-frequency-in-a-sorted-array/
# Python 3 program to count
# occurrences of an element

# A recursive binary search
# function. It returns location
# of x in given array arr[l..r]
# is present, otherwise -1
def binarySearch(arr, l, r, x):
	if (r < l):
		return -1

	mid = int( l + (r - l) / 2)

	# If the element is present
	# at the middle itself
	if arr[mid] == x:
		return mid

	# If element is smaller than
	# mid, then it can only be
	# present in left subarray
	if arr[mid] > x:
		return binarySearch(arr, l,
							mid - 1, x)

	# Else the element
	# can only be present
	# in right subarray
	return binarySearch(arr, mid + 1,
								r, x)

# Returns number of times
# x occurs in arr[0..n-1]
def countOccurrences(arr, n, x):
	ind = binarySearch(arr, 0, n - 1, x)

	# If element is not present
	if ind == -1:
		return 0

	# Count elements
	# on left side.
	count = 1
	left = ind - 1
	while (left >= 0 and
		arr[left] == x):
		count += 1
		left -= 1

	# Count elements on
	# right side.
	right = ind + 1;
	while (right < n and
		arr[right] == x):
		count += 1
		right += 1

	return count

# Driver code
arr = [ 1, 2, 2, 2, 2,
		3, 4, 7, 8, 8 ]
n = len(arr)
x = 2
print(countOccurrences(arr, n, x))

# This code is contributed
# by ChitraNayal
