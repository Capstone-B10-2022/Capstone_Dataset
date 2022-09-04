# Source: https://www.geeksforgeeks.org/check-array-majority-element/

# Hashing based Python
# program to find if
# there is a majority
# element in input array.

# Returns true if there
# is a majority element
# in a[]
def isMajority(a):
	
	# Insert all elements
	# in a hash table
	mp = {}
	
	for i in a:
		if i in mp: mp[i] += 1
		else: mp[i] = 1
	
	# Check if frequency
	# of any element is
	# n/2 or more.
	for x in mp:
		if mp[x] >= len(a)//2:
			return True
	return False

# Driver code
a = [ 2, 3, 9, 2, 2 ]

print("Yes" if isMajority(a) else "No")

#This code is contributed by Ansu Kumari

