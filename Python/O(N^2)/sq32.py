# Python3 program to perform range queries over range
# queries.
# https://www.geeksforgeeks.org/array-range-queries-range-queries/

# Function to create the record array
def record_sum(record, l, r, n, adder):
	
	for i in range(l, r + 1):
		record[i] += adder

# Driver Code
n = 5
m = 5
arr = [0]*n

# Build query matrix
query = [[1, 1, 2 ],[ 1, 4, 5 ],[2, 1, 2 ],
		[ 2, 1, 3 ],[ 2, 3, 4]]
record = [0]*m

for i in range(m - 1, -1, -1):
	
	# If query is of type 2 then function
	# call to record_sum
	if (query[i][0] == 2):
		record_sum(record, query[i][1] - 1,
				query[i][2] - 1, m, record[i] + 1)
		
	# If query is of type 1 then simply add
	# 1 to the record array
	else:
		record_sum(record, i, i, m, 1)
		
# for type 1 queries adding the contains of
# record array to the main array record array
for i in range(m):
	if (query[i][0] == 1):
		record_sum(arr, query[i][1] - 1,
			query[i][2] - 1, n, record[i])

# printing the array
for i in range(n):
	print(arr[i], end=' ')

# This code is contributed by shubhamsingh10
