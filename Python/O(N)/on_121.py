# Source: https://www.geeksforgeeks.org/given-an-array-a-and-a-number-x-check-for-pair-in-a-with-sum-as-x/

def findSum(arr, n, target):

	mp = {}
	result = [0]*2
	for i in range(n):

		findElement = target-arr[i]
		if(findElement in mp):
			result[0] = mp[findElement]
			result[1] = i
			break

		else:
			mp[arr[i]] = i
	return result

# driver code
arr = [1,5,4,3,7,9,2]
n = len(arr)
search = 7
ans = findSum(arr,n,search)
print(f"{min(ans[0], ans[1])} {max(ans[0], ans[1])}")

# This code is contributed by shinjanpatra
