# Python 3 program to find the scalar
# product of a matrix
#https://www.geeksforgeeks.org/program-for-scalar-multiplication-of-a-matrix/
# Size of given matrix
N = 3

def scalarProductMat( mat, k):

	# scalar element is multiplied
	# by the matrix
	for i in range( N):
		for j in range( N):
			mat[i][j] = mat[i][j] * k	

# Driver code
if __name__ == "__main__":
	
	mat = [[ 1, 2, 3 ],
		[ 4, 5, 6 ],
		[ 7, 8, 9 ]]
	k = 4

	scalarProductMat(mat, k)

	# to display the resultant matrix
	print("Scalar Product Matrix is : ")
	for i in range(N):
		for j in range(N):
			print(mat[i][j], end = " ")
		print()

# This code is contributed by ita_c
