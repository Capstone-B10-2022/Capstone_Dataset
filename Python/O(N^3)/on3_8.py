# Source: https://www.geeksforgeeks.org/c-program-multiply-two-matrices/

# 4x4 matrix multiplication using Python3
# Function definition
def matrix_multiplication(M, N):
	# List to store matrix multiplication result
	R = [[0, 0, 0, 0],
		[0, 0, 0, 0],
		[0, 0, 0, 0],
		[0, 0, 0, 0]]

	for i in range(0, 4):
		for j in range(0, 4):
			for k in range(0, 4):
				R[i][j] += M[i][k] * N[k][j]

	for i in range(0, 4):
		for j in range(0, 4):
			# if we use print(), by default cursor moves to next line each time,
			# Now we can explicitly define ending character or sequence passing
			# second parameter as end ="<character or string>"
			# syntax: print(<variable or value to print>, end ="<ending with>")
			# Here space (" ") is used to print a gap after printing
			# each element of R
			print(R[i][j], end =" ")
		print("\n", end ="")

# First matrix. M is a list
M = [[1, 1, 1, 1],
	[2, 2, 2, 2],
	[3, 3, 3, 3],
	[4, 4, 4, 4]]

# Second matrix. N is a list
N = [[1, 1, 1, 1],
	[2, 2, 2, 2],
	[3, 3, 3, 3],
	[4, 4, 4, 4]]
	
# Call matrix_multiplication function
matrix_multiplication(M, N)

# This code is contributed by Santanu
