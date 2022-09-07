# Python3 code to move matrix elements
# in given direction with add
# element with same value
#https://www.geeksforgeeks.org/move-matrix-elements-given-direction-add-elements-value/
MAX = 50

# Function to shift the matrix
# in the given direction
def moveMatrix(d, n, a):

	# For right shift move.
	if (d[0] == 'r'):

		# For each row from
		# top to bottom
		for i in range(n):
			v = []
			w = []

			# For each element of
			# row from right to left
			for j in range(n - 1, -1, -1):
				
				# if not 0
				if (a[i][j]):
					v.append(a[i][j])

			# For each temporary array
			j = 0
			while (j < len(v)):
				
				# If two element have same
				# value at consecutive position.
				if (j < len(v) - 1 and
				v[j] == v[j + 1]):
					
					# Insert only one element
					# as sum of two same element.
					w.append(2 * v[j])
					j += 1
				
				else:
					w.append(v[j])
					
				j += 1

			# Filling the each row element to 0.
			for j in range(n):
				a[i][j] = 0

			j = n - 1

			# Copying the temporary
			# array to the current row.
			for it in w:
				a[i][j] = it
				j -= 1

	# For left shift move
	elif (d[0] == 'l'):

		# For each row
		for i in range(n):
			v = []
			w = []

			# For each element of the
			# row from left to right
			for j in range(n):
				
				# If not 0
				if (a[i][j]):
					v.append(a[i][j])

			# For each temporary array
			j = 0
			while(j < len(v)):
				
				# If two element have same
				# value at consecutive position.
				if (j < len(v) - 1 and
				v[j] == v[j + 1]):
					
					# Insert only one element
					# as sum of two same element.
					w.append(2 * v[j])
					j += 1
				
				else:
					w.append(v[j])
					
				j += 1

			# Filling the each row element to 0.
			for j in range(n):
				a[i][j] = 0

			j = 0

			for it in w:
				a[i][j] = it
				j += 1

	# For down shift move.
	elif (d[0] == 'd'):
		
		# For each column
		for i in range(n):
			v = []
			w = []

			# For each element of
			# column from bottom to top
			for j in range(n - 1, -1, -1):
				
				# If not 0
				if (a[j][i]):
					v.append(a[j][i])

			# For each temporary array
			j = 0
			while(j < len(v)):

				# If two element have same
				# value at consecutive position.
				if (j <len( v) - 1 and
				v[j] == v[j + 1]):
					
					# Insert only one element
					# as sum of two same element.
					w.append(2 * v[j])
					j += 1
				
				else:
					w.append(v[j])
					
				j += 1
					
			# Filling the each column element to 0.
			for j in range(n):
				a[j][i] = 0

			j = n - 1

			# Copying the temporary array
			# to the current column
			for it in w:
				a[j][i] = it
				j -= 1
				
	# For up shift move
	elif (d[0] == 'u'):
		
		# For each column
		for i in range(n):
			v = []
			w = []

			# For each element of column
			# from top to bottom
			for j in range(n):
				
				# If not 0
				if (a[j][i]):
					v.append(a[j][i])

			# For each temporary array
			j = 0
			while(j < len(v)):
				
				# If two element have same
				# value at consecutive position.
				if (j < len(v) - 1 and
				v[j] == v[j + 1]):
					
					# Insert only one element
					# as sum of two same element.
					w.append(2 * v[j])
					j += 1
				
				else:
					w.append(v[j])
				j += 1

			# Filling the each column element to 0.
			for j in range(n):
				a[j][i] = 0

			j = 0

			# Copying the temporary array
			# to the current column
			for it in w:
				a[j][i] = it
				j += 1

# Driver Code
if __name__ == "__main__":

	d = ["l"] * 2
	n = 5
	a = [ [ 32, 3, 3, 3, 3 ],
		[ 0, 0, 1, 0, 0 ],
		[ 10, 10, 8, 1, 2 ],
		[ 0, 0, 0, 0, 1 ],
		[ 4, 5, 6, 7, 8 ] ]

	moveMatrix(d, n, a)

	# Printing the final array
	for i in range(n):
		for j in range(n):
			print(a[i][j], end = " ")

		print()

# This code is contributed by chitranayal
