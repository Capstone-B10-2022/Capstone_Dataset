#https://www.techiedelight.com/find-floor-ceil-number-sorted-array/
# Function to find the ceil of `x` in a sorted list `nums`,
# i.e., the smallest integer greater than or equal to `x`
def getCeil(nums, x):

	# search space is nums[left…right]
	(left, right) = (0, len(nums) - 1)

	# initialize ceil to -1
	ceil = -1

	# loop till the search space is exhausted
	while left <= right:

		# find the mid-value in the search space
		mid = (left + right) // 2

		# if `x` is equal to the middle element, it is the ceil
		if nums[mid] == x:
			return nums[mid]

		# if `x` is less than the middle element, the ceil exists in the
		# sublist nums[left…mid]; update ceil to the middle element
		# and reduce our search space to the left sublist nums[left…mid-1]
		elif x < nums[mid]:
			ceil = nums[mid]
			right = mid - 1

		# if `x` is more than the middle element, the ceil exists in the
		# right sublist nums[mid+1…right]
		else:
			left = mid + 1

	return ceil


# Function to find the floor of `x` in a sorted list `nums`,
# i.e., the largest integer less than or equal to `x`
def getFloor(nums, x):

	(left, right) = (0, len(nums) - 1)

	# initialize floor to -1
	floor = -1

	# loop till the search space is exhausted
	while left <= right:

		# find the mid-value in the search space
		mid = (left + right) // 2

		# if `x` is equal to the middle element, it is the floor
		if nums[mid] == x:
			return nums[mid]

		# if `x` is less than the middle element, the floor exists in the left
		# sublist nums[left…mid-1]
		elif x < nums[mid]:
			right = mid - 1

		# if `x` is more than the middle element, the floor exists in the
		# sublist nums[mid…right]; update floor to the middle element
		# and reduce our search space to the right sublist nums[mid+1…right]
		else:
			floor = nums[mid]
			left = mid + 1

	return floor


if __name__ == '__main__':

	nums = [1, 4, 6, 8, 9]

	for i in range(max(nums) + 2):
		print(f'Number {i} —> ceil is {getCeil(nums, i)},floor is {getFloor(nums, i)}')
