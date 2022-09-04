# Source: https://www.geeksforgeeks.org/find-the-two-repeating-elements-in-a-given-array/

# Python3 code to Find the
# two repeating elements
# in a given array
def printRepeating(arr, size):
	
	# Will hold xor
	# of all elements
	xor = arr[0]
	n = size - 2
	x = 0
	y = 0
	
	# Get the xor of all
	# elements in arr[]
	# and 1, 2 .. n
	for i in range(1 , size):
		xor ^= arr[i]
	for i in range(1 , n + 1):
		xor ^= i
	
	# Get the rightmost set
	# bit in set_bit_no
	set_bit_no = xor & ~(xor-1)
	
	# Now divide elements in two
	# sets by comparing rightmost
	# set bit of xor with bit at
	# same position in each element.
	for i in range(0, size):
		
		if(arr[i] & set_bit_no):
			
			# XOR of first
			# set in arr[]
			x = x ^ arr[i]
		else:
			
			# XOR of second
			# set in arr[]
			y = y ^ arr[i]
			
	for i in range(1 , n + 1):

		if(i & set_bit_no):
			
			# XOR of first set
			# in arr[] and
			# 1, 2, ...n
			x = x ^ i
		else:
			
			# XOR of second set
			# in arr[] and
			# 1, 2, ...n
			y = y ^ i
			
	print("The two repeating",
		"elements are", y, x)

# Driver code	
arr = [4, 2, 4,
	5, 2, 3, 1]
arr_size = len(arr)
printRepeating(arr, arr_size)

# This code is contributed
# by Smitha
