# Source: https://www.geeksforgeeks.org/product-maximum-first-array-minimum-second/

# Python3 program to find the to
# calculate the product of
# max element of first array
# and min element of second array

# Function to calculate the product
def minMaxProduct(arr1, arr2,
				n1, n2) :

	# Initialize max of first array
	max = arr1[0]

	# initialize min of second array
	min = arr2[0]
	
	i = 1
	while (i < n1 and i < n2) :
	
		# To find the maximum
		# element in first array
		if (arr1[i] > max) :
			max = arr1[i]

		# To find the minimum
		# element in second array
		if (arr2[i] < min) :
			min = arr2[i]
		
		i += 1

	# Process remaining elements
	while (i < n1) :
	
		if (arr1[i] > max) :
			max = arr1[i]
			i += 1
	
	while (i < n2):
	
		if (arr2[i] < min) :
			min = arr2[i]
			i += 1

	return max * min

# Driver code
arr1 = [10, 2, 3, 6, 4, 1 ]
arr2 = [5, 1, 4, 2, 6, 9 ]
n1 = len(arr1)
n2 = len(arr1)
print(minMaxProduct(arr1, arr2, n1, n2))

# This code is contributed by Smitha
