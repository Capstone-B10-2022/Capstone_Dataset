# Source: https://www.geeksforgeeks.org/array-range-queries-elements-frequency-value/

# Python 3 Program to answer Q queries
# to find number of times an element x
# appears x times in a Query subarray
import math as mt

# Returns the count of number x with
# frequency x in the subarray from
# start to end
def solveQuery(start, end, arr):

	# map for frequency of elements
	frequency = dict()

	# store frequency of each element
	# in arr[start end]
	for i in range(start, end + 1):


		if arr[i] in frequency.keys():
			frequency[arr[i]] += 1
		else:
			frequency[arr[i]] = 1
				
	# Count elements with same
	# frequency as value
	count = 0
	for x in frequency:
		if x == frequency[x]:
			count += 1
	return count

# Driver code
A = [1, 2, 2, 3, 3, 3 ]
n = len(A)

# 2D array of queries with 2 columns
queries = [[ 0, 1 ], [ 1, 1 ],
		[ 0, 2 ], [ 1, 3 ],
		[ 3, 5 ], [ 0, 5 ]]

# calculating number of queries
q = len(queries)

for i in range(q):
	start = queries[i][0]
	end = queries[i][1]
	print("Answer for Query ", (i + 1),
		" = ", solveQuery(start,end, A))
		
# This code is contributed
# by Mohit kumar 29
