# Source: https://www.geeksforgeeks.org/find-the-two-repeating-elements-in-a-given-array/

# Python3 code for Find the two repeating
# elements in a given array
import math

def printRepeating(arr, size) :
	
	# S is for sum of elements in arr[]
	S = 0;
	
	# P is for product of elements in arr[]
	P = 1;
	
	n = size - 2

	# Calculate Sum and Product
	# of all elements in arr[]
	for i in range(0, size) :
		S = S + arr[i]
		P = P * arr[i]
	
	# S is x + y now
	S = S - n * (n + 1) // 2
	
	# P is x*y now
	P = P // fact(n)	
	
	# D is x - y now
	D = math.sqrt(S * S - 4 * P)
	
	x = (D + S) // 2
	y = (S - D) // 2
	
	print("The two Repeating elements are ",
		(int)(x)," & " ,(int)(y))
	

def fact(n) :
	if(n == 0) :
		return 1
	else :
		return(n * fact(n - 1))

# Driver code
arr = [4, 2, 4, 5, 2, 3, 1]
arr_size = len(arr)
printRepeating(arr, arr_size)

		
# This code is contributed by Nikita Tiwari.
