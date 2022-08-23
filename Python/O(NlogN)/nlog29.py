# Python3 program to do range minimum
# query using sparse table
#https://www.geeksforgeeks.org/sparse-table/
import math

# Fills lookup array lookup[][] in
# bottom up manner.
def buildSparseTable(arr, n):

	# GCD of single element is element itself
	for i in range(0, n):
		table[i][0] = arr[i]

	# Build sparse table
	j = 1
	while (1 << j) <= n:
		i = 0
		while i <= n - (1 << j):
			table[i][j] = math.gcd(table[i][j - 1],
								table[i + (1 << (j - 1))][j - 1])
			
			i += 1
		j += 1

# Returns minimum of arr[L..R]
def query(L, R):

	# Find highest power of 2 that is smaller
	# than or equal to count of elements in
	# given range. For [2, 10], j = 3
	j = int(math.log2(R - L + 1))

	# Compute GCD of last 2^j elements with
	# first 2^j elements in range.
	# For [2, 10], we find GCD of arr[lookup[0][3]]
	# and arr[lookup[3][3]],
	return math.gcd(table[L][j],
					table[R - (1 << j) + 1][j])
	
# Driver Code
if __name__ == "__main__":

	a = [7, 2, 3, 0, 5, 10, 3, 12, 18]
	n = len(a)
	MAX = 500
	
	# lookup[i][j] is going to store minimum
	# value in arr[i..j]. Ideally lookup table
	# size should not be fixed and should be
	# determined using n Log n. It is kept
	# constant to keep code simple.
	table = [[0 for i in range(MAX)]
				for j in range(MAX)]

	buildSparseTable(a, n)
	print(query(0, 2))
	print(query(1, 3))
	print(query(4, 5))
	
# This code is contributed by Rituraj Jain
