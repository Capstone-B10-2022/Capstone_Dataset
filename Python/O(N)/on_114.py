# Source: https://www.geeksforgeeks.org/construct-array-pair-sum-array/

# Fills element in arr[] from its
# pair sum array pair[].
# n is size of arr[]

def constructArr(arr,pair,n):
	arr [0] = (pair[0]+pair[1]-pair[n-1])//2
	for i in range(1,n):
		arr[i] = pair[i-1]-arr[0]

# Driver code
if __name__=='__main__':
	pair = [15, 13, 11, 10, 12, 10, 9, 8, 7, 5]
	n =5
	arr = [0]*n
	constructArr(arr,pair,n)
	for i in range(n):
		print(arr[i],end =" ")

# This code is contributed by
# Shrikant13
