# Python3 program for the above approach

#https://www.geeksforgeeks.org/python3-program-to-generate-a-matrix-having-sum-of-secondary-diagonal-equal-to-a-perfect-square/
# Function to print the matrix whose sum
# of element in secondary diagonal is a
# perfect square
def diagonalSumPerfectSquare(arr, N):
	
	# Print the current row
	print(*arr, sep =" ")
	
	# Iterate for next N - 1 rows
	for i in range(N-1):
		
		# Perform left shift by 1
		arr = arr[i::] + arr[:i:]
		
		# Print the current row after
		# the left shift
		print(*arr, sep =" ")

# Driver Code

# Given N
N = 7

arr = []

# Fill the array with elements
# ranging from 1 to N
for i in range(1, N + 1):
	arr.append(i)

# Function Call
diagonalSumPerfectSquare(arr, N)
