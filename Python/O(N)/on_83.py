# Source: https://www.geeksforgeeks.org/queries-counts-array-elements-values-given-range/

# function to count elements within given range
def countInRange(arr, n, x, y):
 
    # initialize result
    count = 0;
 
    for i in range(n):
 
        # check if element is in range
        if (arr[i] >= x and arr[i] <= y):
            count += 1
    return count
 
# driver function
arr = [1, 3, 4, 9, 10, 3]
n = len(arr)
 
# Answer queries
i = 1
j = 4
print(countInRange(arr, n, i, j))
i = 9
j = 12
print(countInRange(arr, n, i, j))