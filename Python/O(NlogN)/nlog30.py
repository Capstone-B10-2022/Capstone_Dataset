# Python3 program to find the sum in a given
# range in an array using sparse table.
#https://www.geeksforgeeks.org/range-sum-query-using-sparse-table/

# Because 2^17 is larger than 10^5
k = 16

# Maximum value of array
n = 100000

# k + 1 because we need to access
# table[r][k]

table = [[0 for j in range(k+1)] for i in range(n)]

# it builds sparse table
def buildSparseTable(arr, n):
	global table, k
	for i in range(n):
		table[i][0] = arr[i]

	for j in range(1,k+1):
		for i in range(0,n-(1<<j)+1):
			table[i][j] = table[i][j-1] + \
						table[i + (1 << (j - 1))][j - 1]

# Returns the sum of the elements in the range
# L and R.
def query(L, R):
	global table, k

	# boundaries of next query, 0 - indexed
	answer = 0
	for j in range(k,-1,-1):
		if (L + (1 << j) - 1 <= R):
			answer = answer + table[L][j]

			# instead of having L ', we
			# increment L directly
			L+=1<<j

	return answer

# Driver program
if __name__ == '__main__':
	arr = [3, 7, 2, 5, 8, 9]
	n = len(arr)

	buildSparseTable(arr, n)
	print(query(0,5))
	print(query(3,5))
	print(query(2,4))
	
# This code is contributed by
# chaudhary_19 (Mayank Chaudhary)
