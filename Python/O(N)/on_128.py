# Source: https://www.geeksforgeeks.org/maximum-equilibrium-sum-in-an-array/

# Python3 program to find
# maximum equilibrium sum.

# Function to find maximum
# equilibrium sum.
def findMaxSum(arr, n):

	# Array to store prefix sum.
	preSum = [0 for i in range(n)]

	# Array to store suffix sum.
	suffSum = [0 for i in range(n)]

	# Variable to store maximum sum.
	ans = -10000000

	# Calculate prefix sum.
	preSum[0] = arr[0]
	
	for i in range(1, n):
	
		preSum[i] = preSum[i - 1] + arr[i]

	# Calculate suffix sum and compare
	# it with prefix sum. Update ans
	# accordingly.
	suffSum[n - 1] = arr[n - 1]
	if (preSum[n - 1] == suffSum[n - 1]):
		ans = max(ans, preSum[n - 1])
	
	for i in range(n - 2, -1, -1):
		suffSum[i] = suffSum[i + 1] + arr[i]
		if (suffSum[i] == preSum[i]):
			ans = max(ans, preSum[i])
	
	return ans

# Driver Code
if __name__=='__main__':

	arr = [-2, 5, 3, 1,2, 6, -4, 2]
	n = len(arr)
	print(findMaxSum(arr, n))
	
# This code i contributed by pratham76
