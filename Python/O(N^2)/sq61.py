# Function to rotate matrix anticlockwise by 90 degrees.
#https://www.geeksforgeeks.org/rotate-matrix-90-degree-without-using-extra-space-set-2/
def rotateby90(arr):

	n = len(arr)
	if(n%2 == 0):
		mid = n//2-1
	else:
		mid = n/2
	
	j=n-1
	# iterate over all the boundaries of the matrix
	for i in range(mid+1):
		
		for k in range(j-i):
			arr[i][j-k],arr[j][i+k] = arr[j][i+k],arr[i][j-k]
			arr[i+k][i],arr[j][i+k] = arr[j][i+k],arr[i+k][i]
			arr[i][j-k],arr[j-k][j] = arr[j-k][j],arr[i][j-k]
			
		j=j-1
			

# Function for print matrix
def printMatrix(arr):

	for i in range(len(arr)):
			for j in range(len(arr[0])):
				print(arr[i][j] ,end = " ")
			print()
	

# Driver program to test above function
arr=[[ 1, 2, 3, 4 ],
	[ 5, 6, 7, 8 ],
	[ 9, 10, 11, 12 ],
	[ 13, 14, 15, 16 ]]
rotateby90(arr)
printMatrix(arr)

# this code is contributed by CodeWithMini
