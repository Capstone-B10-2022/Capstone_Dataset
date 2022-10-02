# Source: https://www.geeksforgeeks.org/count-pairs-difference-equal-k/



MAX = 100000;
def countPairsWithDiffK(arr, n, k):
	count = 0; # Initialize count

	# Initialize empty hashmap.
	hashmap = [False for i in range(MAX)];

	# Insert array elements to hashmap
	for i in range(n):
		hashmap[arr[i]] = True;

	for i in range(n):
		x = arr[i];
		if (x - k >= 0 and hashmap[x - k]):
			count+=1;
		if (x + k < MAX and hashmap[x + k]):
			count+=1;
		hashmap[x] = False;
	
	return count;

# This code is contributed by 29AjayKumar
