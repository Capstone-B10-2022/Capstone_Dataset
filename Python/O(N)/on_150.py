# Source: https://www.geeksforgeeks.org/squares-of-matrix-diagonal-elements/

# Efficient Python program
# to print squares of
# diagonal elements.

# function of diagonal square
def diagonalsquare(mat, row,
				column) :
	
	# This loop is for finding
	# of square of the first
	# side of diagonal elements
	print ("Diagonal one : ",
					end = "")
	for i in range(0, row) :

		# printing direct square
		# of diagonal element
		# there is no need to
		# check condition
		print (mat[i][i] *
			mat[i][i], end = " ")
	

	# This loop is for finding
	# square of the second side
	# of diagonal elements
	print ("\n\nDiagonal two : ",
						end = "")
	
	for i in range(0, row) :	
		
		# printing direct square
		# of diagonal element in
		# the second side
		print (mat[i][row - i - 1] *
			mat[i][row - i - 1] ,
						end = " ")

# Driver code
mat = [[2, 5, 7 ],
	[3, 7, 2 ],
	[5, 6, 9 ]]
diagonalsquare(mat, 3, 3)
	
# This code is contributed by
# Manish Shaw(manishshaw1)
