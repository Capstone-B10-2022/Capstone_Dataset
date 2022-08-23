# Source: https://www.geeksforgeeks.org/array-range-queries-range-queries/

# Python3 program to perform range
# queries over range queries.

# Function to execute type 1 query
def type1(arr, start, limit):
	
	# incrementing the array by 1
	# for type 1 queries
	for i in range(start, limit + 1):
		arr[i] += 1

# Function to execute type 2 query
def type2(arr, query, start, limit):

	for i in range(start, limit + 1):

		# If the query is of type 1
		# function call to type 1 query
		if (query[i][0] == 1):
			type1(arr, query[i][1], query[i][2])

		# If the query is of type 2
		# recursive call to type 2 query
		else if (query[i][0] == 2):
			type2(arr, query, query[i][1],
							query[i][2])

# Driver code

# Input size of array and
# number of queries
n = 5
m = 5
arr = [0 for i in range(n + 1)]

# Build query matrix
temp = [1, 1, 2, 1, 4, 5, 2,
		1, 2, 2, 1, 3, 2, 3, 4 ]

query = [[0 for i in range(3)]
			for j in range(6)]

j = 0
for i in range(1, m + 1):
	query[i][0] = temp[j]
	j += 1
	query[i][1] = temp[j]
	j += 1
	query[i][2] = temp[j]
	j += 1

# Perform queries
for i in range(1, m + 1):
	if (query[i][0] == 1):
		type1(arr, query[i][1],
				query[i][2])
	else if (query[i][0] == 2):
		type2(arr, query, query[i][1],
						query[i][2])

# printing the result
for i in range(1, n + 1):
	print(arr[i], end = " ")

# This code is contributed
# by mohit kumar
