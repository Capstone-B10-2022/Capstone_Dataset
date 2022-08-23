# Python3 program to perform range
# queries over range queries.
# https://www.geeksforgeeks.org/array-range-queries-range-queries/
import math

max = 10000

# For prefix sum array
def update(arr, l):
	
	arr[l] += arr[l - 1]

# This function is used to apply square root
# decomposition in the record array
def record_func(block_size, block,
				record, l, r, value):

	# Traversing first block in range
	while (l < r and
		l % block_size != 0 and
		l != 0):
		record[l] += value
		l += 1

	# Traversing completely overlapped
	# blocks in range
	while (l + block_size <= r + 1):
		block[l // block_size] += value
		l += block_size

	# Traversing last block in range
	while (l <= r):
		record[l] += value
		l += 1

# Function to print the resultant array
def print_array(arr, n):
	
	for i in range(n):
		print(arr[i], end = " ")

# Driver code
if __name__ == "__main__":

	n = 5
	m = 5
	arr = [0] * n
	record = [0] * m
	
	block_size = (int)(math.sqrt(m))
	block = [0] * max
	
	command = [ [ 1, 1, 2 ],
				[ 1, 4, 5 ],
				[ 2, 1, 2 ],
				[ 2, 1, 3 ],
				[ 2, 3, 4 ] ]

	for i in range(m - 1, -1, -1):

		# If query is of type 2 then function
		# call to record_func
		if (command[i][0] == 2):
			x = i // (block_size)
			
			record_func(block_size, block,
						record, command[i][1] - 1,
								command[i][2] - 1,
						(block[x] + record[i] + 1))

		# If query is of type 1 then simply add
		# 1 to the record array
		else:
			record[i] += 1

	# Merging the value of the block
	# in the record array
	for i in range(m):
		check = (i // block_size)
		record[i] += block[check]

	for i in range(m):
		
		# If query is of type 1 then the array
		# elements are over-written by the record
		# array
		if (command[i][0] == 1):
			arr[command[i][1] - 1] += record[i]
			
			if ((command[i][2] - 1) < n - 1):
				arr[(command[i][2])] -= record[i]

	# The prefix sum of the array
	for i in range(1, n):
		update(arr, i)

	# Printing the resultant array
	print_array(arr, n)

# This code is contributed by chitranayal
