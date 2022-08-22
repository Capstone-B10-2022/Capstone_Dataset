# Python3 program to rearrange positive
# and negative numbers

# Print array function
def printArray(a, n):
	for i in a:
		print(i, end = " ")
	print()


# Driver code
arr = [1, -3, 5, 6, -3, 6, 7, -4, 9, 10]
n = len(arr)

# before modification
printArray(arr, n)

for i in range(n):

	if(arr[i] >= 0 and i % 2 == 1):

		# out of order positive element
		for j in range(i + 1, n):

			if(arr[j] < 0 and j % 2 == 0):
				
				# find out of order negative
				# element in remaining array
				arr[i], arr[j] = arr[j], arr[i]
				break
			
	elif (arr[i] < 0 and i % 2 == 0):
		
		# out of order negative element
		for j in range(i + 1, n):

			if(arr[j] >= 0 and j % 2 == 1):
				
				# find out of order positive
				# element in remaining array
				arr[i], arr[j] = arr[j], arr[i]
				break

# after modification
printArray(arr, n);

# This code is contributed
# by mohit kumar
