# Python3 program to find distinct elements
# common to all rows of a matrix
#https://www.geeksforgeeks.org/find-distinct-elements-common-rows-matrix/
MAX = 100

# function to individually sort
# each row in increasing order
def findAndPrintCommonElements(mat, n):
	us = dict()

	# map elements of first row
	# into 'us'
	for i in range(n):
		us[mat[0][i]] = 1

	for i in range(1, n):
		temp = dict()
		
		# mapping elements of current row
		# in 'temp'
		for j in range(n):
			temp[mat[i][j]] = 1

		# iterate through all the elements
		# of 'us'
		for itr in list(us):

			# if an element of 'us' is not present
			# into 'temp', then erase that element
			# from 'us'
			if itr not in temp:
				del us[itr]

		# if size of 'us' becomes 0,
		# then there are no common elements
		if (len(us) == 0):
			break

	# print common elements
	for itr in list(us)[::-1]:
		print(itr, end = " ")

# Driver Code
mat = [[2, 1, 4, 3],
	[1, 2, 3, 2],
	[3, 6, 2, 3],
	[5, 2, 5, 3]]
n = 4
findAndPrintCommonElements(mat, n)

# This code is contributed by Mohit Kumar
