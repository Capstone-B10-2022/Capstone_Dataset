# Returns count of rotations for an array which
# is first sorted in ascending order, then rotated

#https://www.geeksforgeeks.org/find-rotation-count-rotated-sorted-array/
# Observation: We have to return index of the smallest element


def countRotations(arr, n):

	low = 0
	high = n - 1
	while(low <= high):

		# if first element is mid or
		# last element is mid
		# then simply use modulo
		# so it never goes out of bound.
		mid = low + ((high - low) // 2)
		prev = (mid - 1 + n) % n
		next = (mid + 1) % n

		if(arr[mid] <= arr[prev]
		and arr[mid] <= arr[next]):
			return mid
		elif (arr[mid] <= arr[high]):
			high = mid - 1
		elif (arr[mid] >= arr[low]):
			low = mid + 1
	return 0

# Driver code


arr = [15, 18, 2, 3, 6, 12]
n = len(arr)
print(countRotations(arr, n))

# This code is contributed by shinjanpatra.
