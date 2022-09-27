# Python3 program to find the only
# repeating element in an array where
# elements are from 1 to N-1.
#https://www.geeksforgeeks.org/find-repetitive-element-1-n-1/

def findRepeating(arr, N):
	for i in range(N):
		for j in range(i + 1, N):
			if (arr[i] == arr[j]):
				return arr[i]


# Driver's Code
if __name__ == "__main__":
arr = [9, 8, 2, 6, 1, 8, 5, 3, 4, 7]
N = len(arr)

# Function call
print(findRepeating(arr, N))

# This code is contributed by Arpit Jain
