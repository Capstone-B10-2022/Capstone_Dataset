# Python code to find distinct elements
# common to all rows of a matrix
#https://www.geeksforgeeks.org/find-distinct-elements-common-rows-matrix/
def distinct(matrix, N):
	
	# Make a empty map
	ans = {}

	# Insert the elements of
	# first row in the map and
	# initialize with 1
	for j in range(N):
		ans[matrix[0][j]] = 1

	# Traverse the matrix from 2nd row
	for i in range(N):
		for j in range(N):
			
			# If the element is present in the map
			# and is not duplicated in the current row
			if matrix[i][j] in ans and ans[matrix[i][j]] == i:
				
				# Increment count of the element in
				# map by 1
				ans[matrix[i][j]] = i + 1

				# If we have reached the last row
				if (i == N - 1):
					
					# Print the element
					print(matrix[i][j],end=" ")

# Driver code
matrix = [ [ 2, 1, 4, 3 ],
				[ 1, 2, 3, 2 ],
				[ 3, 6, 2, 3 ],
				[ 5, 2, 5, 3 ] ]
n = 4

distinct(matrix, n)

# This code is contributed by shinjanpatra
