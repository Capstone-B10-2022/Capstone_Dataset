# Python3 program to find Majority
# element in an array
#https://www.geeksforgeeks.org/majority-element/
# Function to find Majority element
# in an array
# it returns -1 if there is no majority element
def majorityElement(arr, n) :
	
	# sort the array in O(nlogn)
	arr.sort()
	count, max_ele, temp, f = 1, -1, arr[0], 0
	for i in range(1, n) :
		
		# increases the count if the same element occurs
		# otherwise starts counting new element
		if(temp == arr[i]) :
			count += 1
		else :
			count = 1
			temp = arr[i]
			
		# sets maximum count
		# and stores maximum occurred element so far
		# if maximum count becomes greater than n/2
		# it breaks out setting the flag
		if(max_ele < count) :
			max_ele = count
			ele = arr[i]
			
			if(max_ele > (n//2)) :
				f = 1
				break
			
	# returns maximum occurred element
	# if there is no such element, returns -1
	if f == 1 :
		return ele
	else :
		return -1

# Driver code
arr = [1, 1, 2, 1, 3, 5, 1]
n = len(arr)

# Function calling
print(majorityElement(arr, n))

# This code is contributed by divyeshrabadiya07
