# Source: https://www.geeksforgeeks.org/number-indexes-equal-elements-given-range/

# Python program to count
# the number of indexes in
# range L R such that Ai=Ai+1
N = 1000

# array to store count
# of index from 0 to
# i that obey condition
prefixans = [0] * N;

# precomputing
# prefixans[] array
def countIndex(a, n) :

	global N, prefixans
	
	# traverse to compute
	# the prefixans[] array
	for i in range(0, n - 1) :

		if (a[i] == a[i + 1]) :
			prefixans[i] = 1

		if (i != 0) :
			prefixans[i] = (prefixans[i] +
							prefixans[i - 1])

# def that answers
# every query in O(1)
def answer_query(l, r) :

	global N, prefixans
	if (l == 0) :
		return prefixans[r - 1]
	else :
		return (prefixans[r - 1] -
				prefixans[l - 1])

# Driver Code
a = [1, 2, 2, 2,
	3, 3, 4, 4, 4]
n = len(a)

# pre-computation
countIndex(a, n)

# 1-st query
L = 1
R = 8

print (answer_query(L, R))

# 2nd query
L = 0
R = 4
print (answer_query(L, R))

# This code is contributed by
# Manish Shaw(manishshaw1)
