# Source: https://www.geeksforgeeks.org/count-minimum-steps-get-given-desired-array/
# Python3 program to count minimum number of
# operations to get the given target array

# Returns count of minimum operations to
# convert a zero array to target array
# with increment and doubling operations.
# This function computes count by doing reverse
# steps, i.e., convert target to zero array.
def countMinOperations(target, n):
	
	# Initialize result (Count of minimum moves)
	result = 0;

	# Keep looping while all elements of
	# target don't become 0.
	while (True):
		
		# To store count of zeroes in
		# current target array
		zero_count = 0;
	
		# To find first odd element
		i = 0;
		while (i < n):
			
			# If odd number found
			if ((target[i] & 1) > 0):
				break;

			# If 0, then increment
			# zero_count
			elif (target[i] == 0):
				zero_count += 1;
			i += 1;

		# All numbers are 0
		if (zero_count == n):
			return result;

		# All numbers are even
		if (i == n):
			
			# Divide the whole array by 2
			# and increment result
			for j in range(n):
				target[j] = target[j] // 2;
			result += 1;

		# Make all odd numbers even by
		# subtracting one and increment result.
		for j in range(i, n):
			if (target[j] & 1):
				target[j] -= 1;
				result += 1;

# Driver Code
arr = [16, 16, 16];
n = len(arr);
print("Minimum number of steps required to",
		"\nget the given target array is",
				countMinOperations(arr, n));

# This code is contributed by mits
