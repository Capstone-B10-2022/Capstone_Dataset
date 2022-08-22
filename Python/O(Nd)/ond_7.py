# Source: https://www.geeksforgeeks.org/k-maximum-sums-non-overlapping-contiguous-sub-arrays/

# Python program to find out k maximum
# non-overlapping subarray sums.
 
# Function to compute k
# maximum sub-array sums.
def kmax(arr, k, n):
 
    # In each iteration it will give
    # the ith maximum subarray sum.
    for c in range(k):
 
        # Kadane's algorithm
        max_so_far = -float("inf")
        max_here = 0
 
        # compute starting and ending
        # index of each of the subarray
        start = 0
        end = 0
        s = 0
        for i in range(n):
             
            max_here += arr[i]
            if (max_so_far < max_here):
                 
                max_so_far = max_here
                start = s
                end = i
            if (max_here < 0):
                 
                max_here = 0
                s = i + 1
 
        # Print out the result
        print("Maximum non-overlapping sub-array sum",
               c + 1, ": ", max_so_far, ", starting index: ",
               start, ", ending index: ", end, ".", sep = "")
 
        # Replace all elements of the maximum subarray
        # by -infinity. Hence these places cannot form
        # maximum sum subarray again.
        for l in range(start, end+1):
            arr[l] = -float("inf")
    print()
 
# Driver Program
# Test case 1
arr1 = [4, 1, 1, -1, -3, -5, 6, 2, -6, -2]
k1 = 3
n1 = len(arr1)
 
# Function calling
kmax(arr1, k1, n1)
 
# Test case 2
arr2 = [5, 1, 2, -6, 2, -1, 3, 1]
k2 = 2
n2 = len(arr2)
 
# Function calling
kmax(arr2, k2, n2)