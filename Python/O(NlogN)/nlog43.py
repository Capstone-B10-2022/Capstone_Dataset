# Python program to print all distinct
# elements in a given array
#https://www.geeksforgeeks.org/print-distinct-elements-given-integer-array/
def printDistinct(arr, n):
	
	# First sort the array so that
	# all occurrences become consecutive
	arr.sort();

	# Traverse the sorted array
	for i in range(n):
		
		# Move the index ahead while there are duplicates
		if(i < n-1 and arr[i] == arr[i+1]):
			while (i < n-1 and (arr[i] == arr[i+1])):
				i+=1;
			

		# print last occurrence of the current element
		else:
			print(arr[i], end=" ");

# Driver code
arr = [6, 10, 5, 4, 9, 120, 4, 6, 10];
n = len(arr);
printDistinct(arr, n);

# This code has been contributed by 29AjayKumar
