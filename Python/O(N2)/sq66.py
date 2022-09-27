# Python3 implementation to print
# the counter clock wise
# spiral traversal of matrix
#https://www.geeksforgeeks.org/print-given-matrix-counter-clock-wise-spiral-form/
#function to print Matrix in CounterClockwise
def counterClockspiralPrint(Matrix):
	size = len(Matrix)
	flag = 0
	k, i = 0, size

	# Print all layers one by one
	while(i > 0):

		# Print First Column of Current Layer
		for j in range(flag,i):
			print(Matrix[j][k], end = ' ')
		i = i - 1
		k = j

		# Print bottom row and last column
		# of current layer
		if (i > 0):
			for j in range(size - i,i + 1):
				print(Matrix[k][j], end = ' ')
			for j in range(k-1,size-i-2,-1):
				print(Matrix[j][k], end = ' ')
		else: break
		k = j
		i = i-1

		# Print top row of current layer
		if (i > 0):
			for j in range(i,size - i-2,-1):
				print(Matrix[k][j], end = ' ')
			k,i = k+1,i+1
			flag = flag + 1
		else: break
	
# Driver code
arr = [ [ 1, 2, 3, 4 ],
		[ 5, 6, 7, 8 ],
		[ 9, 10, 11, 12 ],
		[ 13, 14, 15, 16 ] ]

counterClockspiralPrint(arr)

# This code is contributed by Srihari R
