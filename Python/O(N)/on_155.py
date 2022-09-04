# Source: https://www.geeksforgeeks.org/check-if-array-elements-are-consecutive/

# Function to Check if array
# elements are consecutive
def areConsecutive(arr, n):
	min_ele = arr.index(min(arr))
	num = 0
	for i in range(0, n):
		num ^= arr[min_ele] ^ arr[i]
		arr[min_ele] += 1
	if num == 0:
		return True
	return False

# Driver program to test above
# functions
if __name__ == "__main__":
	arr = [1, 4, 5, 3, 2, 6]
	n = len(arr)
	if areConsecutive(arr, n) == True:
		print(" Array elements are consecutive ", end=' ')
	else:
		print(" Array elements are not consecutive ", end=' ')

# This code is contributed by Aarti_Rathi
