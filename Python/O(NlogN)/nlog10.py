# Python3 code for the above approach

if __name__ == '__main__':
	arr = [12, 3, 5, 7, 19]
	N = len(arr)
	K = 4

	s = set(arr)

	for itr in s:
		if K == 1:
			print(itr) # itr is the Kth element in the set
			break
		K -= 1

# This code is contributed by Abhijeet Kumar(abhijeet19403)
