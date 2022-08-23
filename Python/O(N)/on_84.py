# Source: https://www.geeksforgeeks.org/queries-for-decimal-values-of-subarray-of-a-binary-array/

# implementation of finding number
# represented by binary subarray
from math import pow

# Fills pre[]
def precompute(arr, n, pre):
	
	pre[n - 1] = arr[n - 1] * pow(2, 0)
	i = n - 2
	while(i >= 0):
		pre[i] = (pre[i + 1] + arr[i] *
				(1 << (n - 1 - i)))
		i -= 1

# returns the number represented by
# a binary subarray l to r
def decimalOfSubarr(arr, l, r, n, pre):
	
	# if r is equal to n-1 r+1 does not exist
	if (r != n - 1):
		return ((pre[l] - pre[r + 1]) /
				(1 << (n - 1 - r)))

	return pre[l] / (1 << (n - 1 - r))

# Driver Code
if __name__ == '__main__':
	arr = [1, 0, 1, 0, 1, 1]
	n = len(arr)

	pre = [0 for i in range(n)]
	precompute(arr, n, pre)
	print(int(decimalOfSubarr(arr, 2, 4, n, pre)))
	print(int(decimalOfSubarr(arr, 4, 5, n, pre)))

# This code is contributed by
# Surendra_Gangwar
