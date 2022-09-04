# Source: https://www.geeksforgeeks.org/maximum-triplet-sum-array/

# Python 3 code to find
# maximum triplet sum

def maxTripletSum(arr, n) :

	# Initialize sum with
	# INT_MIN
	sm = -1000000

	for i in range(0, n) :
		for j in range(i + 1, n) :
			for k in range(j + 1, n) :
	
				if (sm < (arr[i] + arr[j] + arr[k])) :
					sm = arr[i] + arr[j] + arr[k]			
	return sm
	
# Driven code
arr = [ 1, 0, 8, 6, 4, 2 ]
n = len(arr)

print(maxTripletSum(arr, n))

# This code is contributed by Nikita Tiwari.
