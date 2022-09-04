# Source: https://www.geeksforgeeks.org/equilibrium-index-of-an-array/

# Python program to find the equilibrium
# index of an array

# Function to find the equilibrium index
def equilibrium(arr):
	left_sum = []
	right_sum = []

	# Iterate from 0 to len(arr)
	for i in range(len(arr)):

		# If i is not 0
		if(i):
			left_sum.append(left_sum[i-1]+arr[i])
			right_sum.append(right_sum[i-1]+arr[len(arr)-1-i])
		else:
			left_sum.append(arr[i])
			right_sum.append(arr[len(arr)-1])

	# Iterate from 0 to len(arr)
	for i in range(len(arr)):
		if(left_sum[i] == right_sum[len(arr) - 1 - i ]):
			return(i)
		
	# If no equilibrium index found,then return -1
	return -1


# Driver code
arr = [-7, 1, 5, 2, -4, 3, 0]
print('First equilibrium index is ',
	equilibrium(arr))

# This code is contributed by Lokesh Sharma
