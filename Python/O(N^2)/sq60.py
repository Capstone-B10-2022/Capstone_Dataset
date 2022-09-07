# Python program to rotate
# a matrix by 90 degrees
#https://www.geeksforgeeks.org/inplace-rotate-square-matrix-by-90-degrees/

def rotateMatrix(mat):

	# reversing the matrix
	for i in range(len(mat)):
		mat[i].reverse()

	# make transpose of the matrix
	for i in range(len(mat)):
		for j in range(i, len(mat)):

			# swapping mat[i][j] and mat[j][i]
			mat[i][j], mat[j][i] = mat[j][i], mat[i][j]


# Function to print the matrix
def displayMatrix(mat):

	for i in range(0, len(mat)):
		for j in range(0, len(mat)):
			print(mat[i][j], end=' ')
		print()


mat = [[1, 2, 3, 4],
	[5, 6, 7, 8],
	[9, 10, 11, 12],
	[13, 14, 15, 16]]

rotateMatrix(mat)

# Print rotated matrix
displayMatrix(mat)

# This code is contributed by shivambhagat02(CC).
