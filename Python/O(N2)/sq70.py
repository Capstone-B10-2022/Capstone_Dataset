# Python3 program to
# rotate a matrix by
# 180 degrees
#https://www.geeksforgeeks.org/rotate-matrix-180-degree/
N = 3;

# Function to Rotate
# the matrix by 180 degree
def rotateMatrix(mat):
	
	# Simply print from
	# last cell to first cell.
	i = N - 1;
	while(i >= 0):
		j = N - 1;
		while(j >= 0):
			print(mat[i][j], end = " ");
			j = j - 1;
		print();
		i = i - 1;

# Driven code
mat = [[1, 2, 3],
	[ 4, 5, 6 ],
	[ 7, 8, 9 ]];
rotateMatrix(mat);

# This code is contributed
# by mits
