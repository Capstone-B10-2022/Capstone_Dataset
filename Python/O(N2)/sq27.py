# Python program to implement above approach
def kthSmallest(mat, n, k):
		
	a = [0 for i in range(n*n)]
	v=0
		
	for i in range(n):
		for j in range(n):
			a[v] = mat[i][j]
			v += 1
			
	a.sort()
	result = a[k - 1]
	return result

# driver program
		
mat = [ [ 10, 20, 30, 40 ],
			[ 15, 25, 35, 45 ],
			[ 25, 29, 37, 48 ],
			[ 32, 33, 39, 50 ] ]
res = kthSmallest(mat, 4, 7)
	
print("7th smallest element is "+ str(res))

# This code is contributed by shinjanpatra
