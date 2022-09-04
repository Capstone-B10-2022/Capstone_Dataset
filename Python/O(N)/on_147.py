# Source: https://www.geeksforgeeks.org/find-subarray-with-given-sum/

# An efficient program
# to print subarray
# with sum as given sum

# Returns true if the
# there is a subarray
# of arr[] with sum
# equal to 'sum'
# otherwise returns
# false. Also, prints
# the result.


def subArraySum(arr, n, sum_):

	# Initialize currentSum as
	# value of first element
	# and starting point as 0
	currentSum = arr[0]
	start = 0

	# Add elements one by
	# one to currentSum and
	# if the currentSum exceeds
	# the sum, then remove
	# starting element
	i = 1
	while i <= n:

		# If currentSum exceeds
		# the sum, then remove
		# the starting elements
		while currentSum > sum_ and start < i-1:

			currentSum = currentSum - arr[start]
			start += 1

		# If currentSum becomes
		# equal to sum, then
		# return true
		if currentSum == sum_:
			print("Sum found between indexes")
			print("% d and % d" % (start, i-1))
			return 1

		# Add this element
		# to currentSum
		if i < n:
			currentSum = currentSum + arr[i]
		i += 1

	# If we reach here,
	# then no subarray
	print("No subarray found")
	return 0


# Driver program
if __name__ == '__main__':
arr = [15, 2, 4, 8, 9, 5, 10, 23]
n = len(arr)
sum_ = 23

subArraySum(arr, n, sum_)

# This code is Contributed by shreyanshi_arun.
