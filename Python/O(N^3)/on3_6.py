# Source: https://www.geeksforgeeks.org/check-rows-matrix-circular-rotations/

# Python3 program to check if all rows
# of a matrix are rotations of each other

MAX = 1000

# Returns true if all rows of mat[0..n-1][0..n-1]
# are rotations of each other.
def isPermutedMatrix(mat, n) :
	
	# Creating a string that contains
	# elements of first row.
	str_cat = ""
	for i in range(n) :
		str_cat = str_cat + "-" + str(mat[0][i])

	# Concatenating the string with itself
	# so that substring search operations
	# can be performed on this
	str_cat = str_cat + str_cat

	# Start traversing remaining rows
	for i in range(1, n) :
		
		# Store the matrix into vector
		# in the form of strings
		curr_str = ""
		
		for j in range(n) :
			curr_str = curr_str + "-" + str(mat[i][j])

		# Check if the current string is present
		# in the concatenated string or not
		if (str_cat.find(curr_str)) :
			return True
			
	return False

# Driver code
if __name__ == "__main__" :
	n = 4
	mat = [[1, 2, 3, 4],
		[4, 1, 2, 3],
		[3, 4, 1, 2],
		[2, 3, 4, 1]]
	
	if (isPermutedMatrix(mat, n)):
		print("Yes")
	else :
		print("No")
		
# This code is contributed by Ryuga
