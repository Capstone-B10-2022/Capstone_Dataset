# Python3 Program to swap diagonal of a matrix
#https://www.geeksforgeeks.org/swap-major-minor-diagonals-square-matrix/
# size of square matrix
N = 3

# Function to swap diagonal of matrix
def swapDiagonal(matrix):
	
	for i in range(N):
		
		matrix[i][i], matrix[i][N-i-1] = \
			matrix[i][N-i-1], matrix[i][i]


# Driver Code
matrix = [[0, 1, 2],
		[3, 4, 5],
		[6, 7, 8]]

# swap diagonals of matrix
swapDiagonal(matrix);

# Displaying modified matrix
for i in range(N):
	for j in range(N):	
		print(matrix[i][j], end = ' ')	
	print()
