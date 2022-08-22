# Source: https://www.geeksforgeeks.org/rearrange-array-arrj-becomes-arri-j/

# A simple Python3 program to rearrange
# contents of arr[] such that arr[j]
# becomes j if arr[i] is j
 
# A simple method to rearrange
# 'arr[0..n-1]' so that 'arr[j]'
# becomes 'i' if 'arr[i]' is 'j'
def rearrangeNaive(arr, n):
 
    # Create an auxiliary array
    # of same size
    temp = [0] * n
     
    # Store result in temp[]
    for i in range(0, n):
        temp[arr[i]] = i
 
    # Copy temp back to arr[]
    for i in range(0, n):
        arr[i] = temp[i]
 
 
    # A utility function to print
    # contents of arr[0..n-1]
def printArray(arr, n):
    for i in range(0, n):
        print(arr[i], end = " ")
 
# Driver program
arr = [1, 3, 0, 2]
n = len(arr)
print("Given array is", end = " ")
printArray(arr, n)
 
rearrangeNaive(arr, n)
print("\nModified array is", end = " ")
printArray(arr, n)