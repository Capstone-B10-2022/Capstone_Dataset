# Python program for the above approach

#https://www.geeksforgeeks.org/java-program-to-find-mth-element-after-k-right-rotations-of-an-array/
# Function to return Mth element of
# array after k left rotations
def getFirstElement(a, N, K, M):

# The array comes to original state
# after N rotations
K %= N
index = 0
if (K >= M):

	# Mth element after k right
	# rotations is (N-K)+(M-1) th
	# element of the array
	index = (N - K) + (M - 1)

# Otherwise
else:

	# (M - K - 1) th element
	# of the array
	index = (M - K - 1)

result = a[index]

# Return the result
return result

# Driver Code

# Array initialization
a = [ 1, 2, 3, 4, 5 ]
N = len(a)
K,M = 3,2

# Function call
print(getFirstElement(a, N, K, M))

# This code is contributed by shinjanpatra
