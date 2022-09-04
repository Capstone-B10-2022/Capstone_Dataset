# Source: https://www.geeksforgeeks.org/find-the-two-repeating-elements-in-a-given-array/

# Python program for the above approach
def twoRepeated(arr, N):
	m = N - 1
	for i in range(N):
		arr[arr[i] % m - 1] += m
		if ((arr[arr[i] % m - 1] // m) == 2):
			print(arr[i] % m ,end= " ")
	
# Driver Code
arr = [4, 2, 4, 5, 2, 3, 1]
n = len(arr)
print("The two repeating elements are ", end = "")
twoRepeated(arr, n)

# This code is contributed by Shubham Singh
