# Python3 program to shift k
# elements in a matrix.
#https://www.geeksforgeeks.org/shift-matrix-elements-k/
N = 4
# Function to shift first k
# elements of each row of
# matrix.
def shiftMatrixByK(mat, k):
	if (k > N) :
		print ("shifting is"
			" not possible")
		return
	
	j = 0
	while (j < N) :
		
		# Print elements from
		# index k
		for i in range(k, N):
			print ("{} " .
			format(mat[j][i]), end="")
			
		# Print elements before
		# index k
		for i in range(0, k):
			print ("{} " .
			format(mat[j][i]), end="")
			
		print ("")
		j = j + 1

# Driver code
mat = [[1, 2, 3, 4],
	[5, 6, 7, 8],
	[9, 10, 11, 12],
	[13, 14, 15, 16]]
k = 2

# Function call
shiftMatrixByK(mat, k)

# This code is contributed by
# Manish Shaw (manishshaw1)
