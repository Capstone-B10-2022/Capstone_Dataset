# A O(n) time and O(1) extra space Python3 program to
# sort an array according to given indexes

# Function to reorder elements of arr[] according
# to index[]
def reorder(arr, index, n):

	# Fix all elements one by one
	for i in range(0,n):

		# While index[i] and arr[i] are not fixed
		while (index[i] != i):
		
			# Store values of the target (or correct)
			# position before placing arr[i] there
			oldTargetI = index[index[i]]
			oldTargetE = arr[index[i]]

			# Place arr[i] at its target (or correct)
			# position. Also copy corrected index for
			# new position
			arr[index[i]] = arr[i]
			index[index[i]] = index[i]

			# Copy old target values to arr[i] and
			# index[i]
			index[i] = oldTargetI
			arr[i] = oldTargetE


# Driver program
arr = [50, 40, 70, 60, 90]
index= [3, 0, 4, 1, 2]
n = len(arr)

reorder(arr, index, n)

print("Reordered array is:")
for i in range(0, n):
	print(arr[i],end=" ")

print("\nModified Index array is:")
for i in range(0, n):
	print(index[i] ,end=" ")

# This code is contributed by
# Smitha Dinesh Semwal
