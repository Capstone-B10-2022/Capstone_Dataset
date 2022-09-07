#https://www.geeksforgeeks.org/count-pairs-difference-equal-k/
def BS(arr, X, low):
    	high = len(arr) - 1;
	ans = len(arr);
	while (low <= high):
		mid = low + (high - low) // 2;
		if (arr[mid] >= X):
			ans = mid;
			high = mid - 1;
		else:
			low = mid + 1;
	
	return ans;

def countPairsWithDiffK(arr, N, k):
	count = 0;
	arr.sort();
	for i in range(N):
		X = BS(arr, arr[i] + k, i + 1);
		if (X != N):
			Y = BS(arr, arr[i] + k + 1, i + 1);
			count += Y - X;
		
	return count;

if __name__ == '__main__':
	arr = [ 1, 3, 5, 8, 6, 4, 6 ];
	n = len(arr);
	k = 2;
	print("Count of pairs with given diff is " , countPairsWithDiffK(arr, n, k));
	
# This code is contributed by shikhasingrajput
