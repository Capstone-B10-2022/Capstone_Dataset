# Source: https://www.geeksforgeeks.org/sort-array-wave-form-2/

# Python function to sort the array arr[0..n-1] in wave form,
# i.e., arr[0] >= arr[1] <= arr[2] >= arr[3] <= arr[4] >= arr[5]
def sortInWave(arr, n):
	
	# Traverse all even elements
	for i in range(0, n, 2):
		
		# If current even element is smaller than previous
		if (i> 0 and arr[i] < arr[i-1]):
			arr[i],arr[i-1] = arr[i-1],arr[i]
		
		# If current even element is smaller than next
		if (i < n-1 and arr[i] < arr[i+1]):
			arr[i],arr[i+1] = arr[i+1],arr[i]

# Driver program
arr = [10, 90, 49, 2, 1, 5, 23]
sortInWave(arr, len(arr))
for i in range(0,len(arr)):
	print (arr[i],end=" ")
	
# This code is contributed by __Devesh Agrawal__
