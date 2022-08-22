# Python 3 program to rearrange
# positive and negative numbers

def rearrange(a, size) :
	
	positive = 0
	negative = 1

	while (True) :
		
		# Move forward the positive
		# pointer till negative number
		# number not encountered
		while (positive < size and a[positive] >= 0) :
			positive = positive + 2

		# Move forward the negative
		# pointer till positive number
		# number not encountered
		while (negative < size and a[negative] <= 0) :
			negative = negative + 2

		# Swap array elements to fix
		# their position.
		if (positive < size and negative < size) :
			temp = a[positive]
			a[positive] = a[negative]
			a[negative] = temp

		# Break from the while loop when
		# any index exceeds the size of
		# the array
		else :
			break
		
# Driver code
arr =[ 1, -3, 5, 6, -3, 6, 7, -4, 9, 10 ]
n = len(arr)

rearrange(arr, n)
for i in range(0, n) :
	print(arr[i], end = " ")

# This code is contributed by Nikita Tiwari.
