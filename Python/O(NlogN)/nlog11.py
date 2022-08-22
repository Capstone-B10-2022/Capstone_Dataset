# Python3 program for the above approach


def Kth_smallest(mp, K):

	freq = 0
	for it in sorted(mp.keys()):
		freq += mp[it] # adding the frequencies of
		# each element
		if freq >= K: # if at any point frequency becomes
			return it # greater than or equal to k then
			# return that element
	return -1 # returning -1 if k>size of the array which
	# is an impossible scenario


# driver's code
if __name__ == "__main__":
	N = 5
	K = 2
	arr = [12, 3, 5, 7, 19]
	mp = {}
	for i in range(N):
		if arr[i] in mp: # mapping every element with it's
			mp[arr[i]] = mp[arr[i]] + 1 # frequency
		else:
			mp[arr[i]] = 1

	# Function call
	ans = Kth_smallest(mp, K)
	print("The ", K, "th smallest element is ", ans)

# This code is contributed by Abhijeet Kumar(abhijeet19403)
