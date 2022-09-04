# Source: https://www.geeksforgeeks.org/majority-element/

# Python3 program for finding out majority
# element in an array

def findMajority(arr, size):
	m = {}
	for i in range(size):
		if arr[i] in m:
			m[arr[i]] += 1
		else:
			m[arr[i]] = 1
	count = 0
	for key in m:
		if m[key] > size / 2:
			count = 1
			print("Majority found :-",key)
			break
	if(count == 0):
		print("No Majority element")

# Driver code
arr = [2, 2, 2, 2, 5, 5, 2, 3, 3]
n = len(arr)

# Function calling
findMajority(arr, n)

# This code is contributed by ankush_953
