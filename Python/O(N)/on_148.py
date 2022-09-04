# Source: https://www.geeksforgeeks.org/maximum-triplet-sum-array/

# Python 3 code to find
# maximum triplet sum

# This function assumes
# that there are at least
# three elements in arr[].
def maxTripletSum(arr, n) :

	# Initialize Maximum, second
	# maximum and third maximum
	# element
	maxA = -100000000
	maxB = -100000000
	maxC = -100000000

	for i in range(0, n) :
	
		# Update Maximum, second maximum
		# and third maximum element
		if (arr[i] > maxA) :
			maxC = maxB
			maxB = maxA
			maxA = arr[i]

		# Update second maximum and
		# third maximum element
		elif (arr[i] > maxB) :
			maxC = maxB
			maxB = arr[i]
		
		# Update third maximum element
		elif (arr[i] > maxC) :
			maxC = arr[i]
			
	return (maxA + maxB + maxC)
	
# Driven code
arr = [ 1, 0, 8, 6, 4, 2 ]
n = len(arr)

print(maxTripletSum(arr, n))

# This code is contributed by Nikita Tiwari.
