#https://www.geeksforgeeks.org/find-a-peak-in-a-given-array/
#The below-given code is the iterative version of the above explained and demonstrated recursive based divide and conquer technique.
# A Python program to find a peak element
# using divide and conquer

# A binary search based function
# that returns index of a peak element
def findPeak(arr, n):

	l = 0
	r = n-1
	
	while(l <= r):

		# finding mid by binary right shifting.
		mid = (l + r) >> 1

		# first case if mid is the answer
		if((mid == 0 or arr[mid - 1] <= arr[mid]) and (mid == n - 1 or arr[mid + 1] <= arr[mid])):
			break

		# move the right pointer
		if(mid > 0 and arr[mid - 1] > arr[mid]):
			r = mid - 1

		# move the left pointer
		else:
			l = mid + 1

	return mid


# Driver Code
arr = [1, 3, 20, 4, 1, 0]
n = len(arr)
print(f"Index of a peak point is {findPeak(arr, n)}")

# This code is contributed by Rajdeep Mallick (rajdeep999)
