# Source: https://www.geeksforgeeks.org/find-subarray-least-average/

# Python3 program to find
# minimum average subarray

# Prints beginning and ending
# indexes of subarray of size k
# with minimum average
def findsubarrayleast(arr, k, n):
	min = 999999
	minindex = 0
	for i in range(n-k+1):
		sum = 0
		j = i
		for j in range(i, i+k):
			sum += arr[j]
		if sum < min:
			min = sum
			minindex = i

	# printing the desired subarray
	print("subarray with minimum average is: ", end='')
	for i in range(minindex, minindex+k):
		print(arr[i], end=" ")


# Driver Code
arr = [20, 3, 13, 5, 10, 14, 8, 5, 11, 9, 1, 11]
k = 9 # Subarray size
n = len(arr)
findsubarrayleast(arr, k, n)

# This code is contributed by Aarti_Rathi
