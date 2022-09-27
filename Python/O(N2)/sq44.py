# Function to find position to insert current element of
# stream using binary search
# https://www.geeksforgeeks.org/median-of-stream-of-integers-running-integers/
def binarySearch(arr, item, low, high):

	if (low >= high):
		return (low + 1) if (item > arr[low]) else low

	mid = (low + high) // 2

	if (item == arr[mid]):
		return mid + 1

	if (item > arr[mid]):
		return binarySearch(arr, item, mid + 1, high)

	return binarySearch(arr, item, low, mid - 1)

# Function to print median of stream of integers
def printMedian(arr, n):

	i, j, pos, num = 0, 0, 0, 0
	count = 1

	print(f"Median after reading 1 element is {arr[0]}")

	for i in range(1, n):
		median = 0
		j = i - 1
		num = arr[i]

		# find position to insert current element in sorted
		# part of array
		pos = binarySearch(arr, num, 0, j)

		# move elements to right to create space to insert
		# the current element
		while (j >= pos):
			arr[j + 1] = arr[j]
			j -= 1

		arr[j + 1] = num

		# increment count of sorted elements in array
		count += 1

		# if odd number of integers are read from stream
		# then middle element in sorted order is median
		# else average of middle elements is median
		if (count % 2 != 0):
			median = arr[count // 2]

		else:
			median = (arr[(count // 2) - 1] + arr[count // 2]) // 2

		print(f"Median after reading {i + 1} elements is {median} ")

# Driver Code
if __name__ == "__main__":

	arr = [5, 15, 1, 3, 2, 8, 7, 9, 10, 6, 11, 4]
	n = len(arr)

	printMedian(arr, n)

# This code is contributed by rakeshsahni
