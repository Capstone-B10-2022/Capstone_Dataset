# Source: https://www.geeksforgeeks.org/constant-time-range-add-operation-array/

# Python3 program to get updated array
# after many array range add operation
 
# Utility method to add value
# val, to range [lo, hi]
 
 
def add(arr, N, lo, hi, val):
 
    arr[lo] += val
    if (hi != N - 1):
        arr[hi + 1] -= val
 
# Utility method to get actual
# array from operation array
 
 
def updateArray(arr, N):
 
    # convert array into prefix sum array
    for i in range(1, N):
        arr[i] += arr[i - 1]
 
# method to print final updated array
 
 
def printArr(arr, N):
 
    updateArray(arr, N)
    for i in range(N):
        print(arr[i], end=" ")
    print()
 
 
# Driver code
N = 6
arr = [0 for i in range(N)]
 
# Range add Queries
add(arr, N, 0, 2, 100)
add(arr, N, 1, 5, 100)
add(arr, N, 2, 3, 100)
 
printArr(arr, N)