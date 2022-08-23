# Python 3 program to Count elements which
# divides all numbers in range L-R
# https://www.geeksforgeeks.org/count-elements-which-divide-all-numbers-in-range-l-r/

# function to count element
# Time complexity O(n^2) worst case
def answerQuery(a, n, l, r):
	
	# answer for query
	count = 0

	# 0 based index
	l = l - 1

	# iterate for all elements
	for i in range(l, r, 1):
		element = a[i]
		divisors = 0

		# check if the element divides
		# all numbers in range
		for j in range(l, r, 1):
			
			# no of elements
			if (a[j] % a[i] == 0):
				divisors += 1
			else:
				break
		
		# if all elements are divisible
		# by a[i]
		if (divisors == (r - l)):
			count += 1

	# answer for every query
	return count

# Driver Code
if __name__ =='__main__':
	a = [1, 2, 3, 5]
	n = len(a)

	l = 1
	r = 4
	print(answerQuery(a, n, l, r))

	l = 2
	r = 4
	print(answerQuery(a, n, l, r))

# This code is contributed by
# Shashank_Sharma
