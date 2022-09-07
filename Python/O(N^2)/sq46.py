# Python implementation of the above approach
#https://www.geeksforgeeks.org/find-number-of-triangles-possible/
def CountTriangles( A):

	n = len(A);

	A.sort();

	count = 0;
	
	for i in range(n - 1, 0, -1):
		l = 0;
		r = i - 1;
		while(l < r):
			if(A[l] + A[r] > A[i]):

				# If it is possible with a[l], a[r]
				# and a[i] then it is also possible
				# with a[l + 1]..a[r-1], a[r] and a[i]
				count += r - l;

				# checking for more possible solutions
				r -= 1;
			
			else:

				# if not possible check for
				# higher values of arr[l]
				l += 1;
	print("No of possible solutions: ", count);

# Driver Code
if __name__ == '__main__':

	A = [ 4, 3, 5, 7, 6 ];

	CountTriangles(A);
	
# This code is contributed by PrinciRaj1992
