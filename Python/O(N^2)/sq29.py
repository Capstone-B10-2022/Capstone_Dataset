# Python3 program to find
# all elements in array
# which have at-least two
# greater elements itself.

def findElements( arr, n):

	# Pick elements one by
		# one and count greater
	# elements. If count
		# is more than 2, print
	# that element.

	for i in range(n):
		count = 0
		for j in range(0, n):
			if arr[j] > arr[i]:
				count = count + 1
						
				
		if count >= 2 :
			print(arr[i], end=" ")
			

# Driver code
arr = [ 2, -6 ,3 , 5, 1]
n = len(arr)
findElements(arr, n)
	
# This code is contributed by sunnysingh
