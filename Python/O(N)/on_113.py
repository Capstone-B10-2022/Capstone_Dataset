# Source: https://www.geeksforgeeks.org/print-distinct-elements-given-integer-array/

# Python3 program to print all distinct elements
# of a given array

# This function prints all distinct elements
def printDistinct(arr, n):
	
	# Creates an empty hashset
	s = dict();

	# Traverse the input array
	for i in range(n):
		
		# If not present, then put it in
		# hashtable and print it
		if (arr[i] not in s.keys()):
			s[arr[i]] = arr[i];
			print(arr[i], end = " ");

# Driver Code
arr = [10, 5, 3, 4, 3, 5, 6];
n = 7;
printDistinct(arr, n);

# This code is contributed by Princi Singh
