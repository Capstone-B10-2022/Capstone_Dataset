# Source: https://www.geeksforgeeks.org/subarraysubstring-vs-subsequence-and-programs-to-generate-them/

# Python3 code to generate all possible
# subarrays/subArrays
# Complexity- O(n^3)

# Prints all subarrays in arr[0..n-1]
def subArray(arr, n):

	# Pick starting point
	for i in range(0,n):

		# Pick ending point
		for j in range(i,n):

			# Print subarray between
			# current starting
			# and ending points
			for k in range(i,j+1):
				print (arr[k],end=" ")

			print ("\n",end="")

			
# Driver program
arr = [1, 2, 3, 4]
n = len(arr)
print ("All Non-empty Subarrays")

subArray(arr, n);

# This code is contributed by Shreyanshi.
