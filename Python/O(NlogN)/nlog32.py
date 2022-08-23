#https://www.geeksforgeeks.org/queries-counts-array-elements-values-given-range/
# function to find first index >= x
def lowerIndex(arr, n, x):
l = 0
h = n-1
while (l <= h):
	mid = int((l + h)//2)
	if (arr[mid] >= x):
	h = mid - 1
	else:
	l = mid + 1
return l


# function to find last index <= x
def upperIndex(arr, n, x):
l = 0
h = n-1
while (l <= h):
	mid = int((l + h)//2)
	if (arr[mid] <= x):
	l = mid + 1
	else:
	h = mid - 1
return h


# function to count elements within given range
def countInRange(arr, n, x, y):
# initialize result
count = 0;
count = upperIndex(arr, n, y) - lowerIndex(arr, n, x) + 1;
return count

# driver function
arr = [1, 3, 4, 9, 10, 3]

# Preprocess array
arr.sort()
n = len(arr)

# Answer queries
i = 1
j = 4
print(countInRange(arr, n, i, j))
i = 9
j = 12
print(countInRange(arr, n, i, j))
