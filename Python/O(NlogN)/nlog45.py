# Python3 program to find the only
# repeating element in an array where
# elements are from 1 to N-1.
#https://www.geeksforgeeks.org/find-repetitive-element-1-n-1/

def findRepeating(arr, N):
	arr.sort()
	for i in range(1, N):
		if(arr[i] != i+1):
			return arr[i]


# Driver's Code
if __name__ == "__main__":
arr = [9, 8, 2, 6, 1, 8, 5, 3, 4, 7]
N = len(arr)

# Function call
print(findRepeating(arr, N))

# This code is contributed by Arpit Jain
