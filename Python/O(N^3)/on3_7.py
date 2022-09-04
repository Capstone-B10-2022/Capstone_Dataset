# Source: https://www.geeksforgeeks.org/c-program-multiply-two-matrices/

# 4x4 matrix multiplication using Python3
# Function definition
def mulMat(mat1, mat2, R1, R2, C1, C2):
	# List to store matrix multiplication result
	rslt = [[0, 0, 0, 0],
			[0, 0, 0, 0],
			[0, 0, 0, 0],
			[0, 0, 0, 0]]

	for i in range(0, R1):
		for j in range(0, C2):
			for k in range(0, R2):
				rslt[i][j] += mat1[i][k] * mat2[k][j]

	for i in range(0, R1):
		for j in range(0, C2):
			print(rslt[i][j], end=" ")
		print("\n", end="")


R1 = 4
R2 = 4
C1 = 4
C2 = 4

# First matrix. M is a list
mat1 = [[1, 1, 1, 1],
		[2, 2, 2, 2],
		[3, 3, 3, 3],
		[4, 4, 4, 4]]

# Second matrix. N is a list
mat2 = [[1, 1, 1, 1],
		[2, 2, 2, 2],
		[3, 3, 3, 3],
		[4, 4, 4, 4]]

if C1 != R2:
	print("The number of columns in Matrix-1 must be equal to the number of rows in " + "Matrix-2", end='')
	print("\n", end='')
	print("Please update MACROs according to your array dimension in #define section", end='')
	print("\n", end='')
else:
	# Call matrix_multiplication function
	mulMat(mat1, mat2, R1, R2, C1, C2)

# This code is contributed by Aarti_Rathi
