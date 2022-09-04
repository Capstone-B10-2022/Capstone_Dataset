# Source: https://www.geeksforgeeks.org/sort-1-n-swapping-adjacent-elements/

# Python3 program to test whether array
# can be sorted by swapping adjacent
# elements using boolean array

# Return true if array can be
# sorted otherwise false
def sortedAfterSwap(A,B,n):
	for i in range(0,n-1):
		if B[i]:
			if A[i]!=i+1:
				A[i], A[i+1] = A[i+1], A[i]

	# Check if array is sorted or not
	for i in range(n):
		if A[i]!=i+1:
			return False
	return True

# Driver program
if __name__=='__main__':
	A = [1, 2, 5, 3, 4, 6]
	B = [0, 1, 1, 1, 0]
	n =len(A)
	if (sortedAfterSwap(A, B, n)) :
		print("A can be sorted")
	else :
		print("A can not be sorted")

# This code is contributed by
# Shrikant13
