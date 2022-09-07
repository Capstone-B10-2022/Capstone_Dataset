# Python 3 program to find maximum
# equilibrium sum.
#https://www.geeksforgeeks.org/maximum-equilibrium-sum-in-an-array/
import sys

# Function to find maximum equilibrium sum.
def findMaxSum(arr, n):
	res = -sys.maxsize - 1
	for i in range(n):
		prefix_sum = arr[i]
		for j in range(i):
			prefix_sum += arr[j]

		suffix_sum = arr[i]
		j = n - 1
		while(j > i):
			suffix_sum += arr[j]
			j -= 1
		if (prefix_sum == suffix_sum):
			res = max(res, prefix_sum)

	return res

# Driver Code
if __name__ == '__main__':
	arr = [-2, 5, 3, 1, 2, 6, -4, 2]
	n = len(arr)
	print(findMaxSum(arr, n))

# This code is contributed by
# Surendra_Gangwar
