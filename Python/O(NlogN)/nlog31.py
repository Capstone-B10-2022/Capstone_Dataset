# Python program for
# queries of GCD excluding
# given range of elements.
#https://www.geeksforgeeks.org/queries-gcd-numbers-array-except-elements-given-range/

# Calculating GCD
# using euclid algorithm
def GCD(a,b):
	if (b==0):
		return a
	return GCD (b, a%b)


# Filling the prefix
# and suffix array
def FillPrefixSuffix(prefix,arr,suffix,n):

	# Filling the prefix array
	# following relation
	# prefix(i) = GCD(prefix(i-1), arr(i))
	prefix[0] = arr[0]
	for i in range(1,n):
		prefix[i] = GCD (prefix[i-1], arr[i])

	# Filling the suffix
	# array following the
	# relation suffix(i) = GCD(suffix(i+1), arr(i))
	suffix[n-1] = arr[n-1]

	for i in range(n-2,-1,-1):
		suffix[i] = GCD (suffix[i+1], arr[i])


# To calculate gcd of
# the numbers outside range
def GCDoutsideRange(l,r,prefix,suffix,n):
	
	# If l=0, we need to tell GCD of numbers
	# from r+1 to n
	if (l==0):
		return suffix[r+1]

	# If r=n-1 we need to return the gcd of
	# numbers from 1 to l
	if (r==n-1):
		return prefix[l-1]
	return GCD(prefix[l-1], suffix[r+1])

# Driver code

arr = [2, 6, 9]
n = len(arr)
prefix=[]
suffix=[]
for i in range(n+1):
	prefix.append(0)
	suffix.append(0)
	
FillPrefixSuffix(prefix, arr, suffix, n)
l = 0
r = 0
print(GCDoutsideRange(l, r, prefix, suffix, n))

l = 1
r = 1
print(GCDoutsideRange(l, r, prefix, suffix, n))

l = 1
r = 2
print(GCDoutsideRange(l, r, prefix, suffix, n))

# This code is contributed
# by Anant Agarwal.
