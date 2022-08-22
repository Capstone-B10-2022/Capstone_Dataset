# Source: https://www.geeksforgeeks.org/k-maximum-sum-overlapping-contiguous-sub-arrays/

# Python program to find out k maximum sum of
# overlapping sub-arrays
 
# Function to compute prefix-sum of the input array
def prefix_sum(arr, n):
    pre_sum = list()
    pre_sum.append(arr[0])
    for i in range(1, n):
        pre_sum.append(pre_sum[i-1] + arr[i])
    return pre_sum
 
# Update maxi by k maximum values from maxi and cand
def maxMerge(maxi, cand):
 
    # Here cand and maxi arrays are in non-increasing
    # order beforehand. Now, j is the index of the
    # next cand element and i is the index of next
    # maxi element. Traverse through maxi array.
    # If cand[j] > maxi[i] insert cand[j] at the ith
    # position in the maxi array and remove the minimum
    # element of the maxi array i.e. the last element
    # and increase j by 1 i.e. take the next element
    # from cand.
    k = len(maxi)
    j = 0
    for i in range(k):
        if (cand[j] > maxi[i]):
            maxi.insert(i, cand[j])
            del maxi[-1]
            j += 1
 
# Insert prefix_sum[i] to mini array if needed
def insertMini(mini, pre_sum):
 
    # Traverse the mini array from left to right.
    # If prefix_sum[i] is less than any element
    # then insert prefix_sum[i] at that position
    # and delete maximum element of the mini array
    # i.e. the rightmost element from the array.
    k = len(mini)
    for i in range(k):
        if (pre_sum < mini[i]):
            mini.insert(i, pre_sum)
            del mini[-1]
            break
 
# Function to compute k maximum overlapping sub-array sums
def kMaxOvSubArray(arr, k):
    n = len(arr)
 
    # Compute the prefix sum of the input array.
    pre_sum = prefix_sum(arr, n)
 
    # Set all the elements of mini as + infinite
    # except 0th. Set the 0th element as 0.
    mini = [float('inf') for i in range(k)]
    mini[0] = 0
 
    # Set all the elements of maxi as -infinite.
    maxi = [-float('inf') for i in range(k)]
 
    # Initialize cand array.
    cand = [0 for i in range(k)]
 
    # For each element of the prefix_sum array do:
    # compute the cand array.
    # take k maximum values from maxi and cand
    # using maxmerge function.
    # insert prefix_sum[i] to mini array if needed
    # using insertMini function.
    for i in range(n):
        for j in range(k):
            cand[j] = pre_sum[i] - mini[j]
        maxMerge(maxi, cand)
        insertMini(mini, pre_sum[i])
 
    # Elements of maxi array is the k
    # maximum overlapping sub-array sums.
    # Print out the elements of maxi array.
    for ele in maxi:
        print(ele, end = ' ')
    print('')
 
# Driver Program
# Test case 1
arr1 = [4, -8, 9, -4, 1, -8, -1, 6]
k1 = 4
kMaxOvSubArray(arr1, k1)
 
# Test case 2
arr2 = [-2, -3, 4, -1, -2, 1, 5, -3]
k2 = 3
kMaxOvSubArray(arr2, k2)