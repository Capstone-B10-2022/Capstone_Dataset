# Source: https://www.geeksforgeeks.org/number-whose-sum-of-xor-with-given-array-range-is-maximum/

# Python3 program to find smallest integer X
# such that sum of its XOR with range is
# maximum.
import math

one = [[0 for x in range(32)]
	for y in range(100001)]
MAX = 2147483647

# Function to make prefix array
# which counts 1's of each bit
# up to that number
def make_prefix(A, n) :
	global one, MAX
	
	for j in range(0 , 32) :
		one[0][j] = 0

	# Making a prefix array which
	# sums number of 1's up to
	# that position
	for i in range(1, n+1) :
		a = A[i - 1]
		for j in range(0 , 32) :
		
			x = int(math.pow(2, j))

			# If j-th bit of a number
			# is set then add one to
			# previously counted 1's
			if (a & x) :
				one[i][j] = 1 + one[i - 1][j]
			else :
				one[i][j] = one[i - 1][j]
		
# Function to find X
def Solve(L, R) :

	global one, MAX
	l = L
	r = R
	tot_bits = r - l + 1

	# Initially taking maximum
	# value all bits 1
	X = MAX

	# Iterating over each bit
	for i in range(0, 31) :
	
		# get 1's at ith bit between the
		# range L-R by subtracting 1's till
		# Rth number - 1's till L-1th number
		
		x = one[r][i] - one[l - 1][i]

		# If 1's are more than or equal
		# to 0's then unset the ith bit
		# from answer
		if (x >= (tot_bits - x)) :
			
			ith_bit = pow(2, i)

			# Set ith bit to 0 by
			# doing Xor with 1
			X = X ^ ith_bit
	return X

# Driver Code
n = 5
q = 3
A = [ 210, 11, 48, 22, 133 ]
L = [ 1, 4, 2 ]
R = [ 3, 14, 4 ]

make_prefix(A, n)

for j in range(0, q) :
	print (Solve(L[j], R[j]),end="\n")
	
# This code is contributed by
# Manish Shaw(manishshaw1)
