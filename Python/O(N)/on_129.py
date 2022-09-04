# Source: https://www.geeksforgeeks.org/maximum-equilibrium-sum-in-an-array/

# Python3 program to find
# maximum equilibrium sum.
import sys

# Function to find
# maximum equilibrium sum.
def findMaxSum(arr,n):
	
	ss = sum(arr)
	prefix_sum = 0
	res = -sys.maxsize
	
	for i in range(n):
		prefix_sum += arr[i]
		
		if prefix_sum == ss:
			res = max(res, prefix_sum);
			
		ss -= arr[i];
		
	return res

# Driver code
if __name__=="__main__":
	
	arr = [ -2, 5, 3, 1,
			2, 6, -4, 2 ]
	n = len(arr)
	
	print(findMaxSum(arr, n))

# This code is contributed by rutvik_56
