# Source: https://www.geeksforgeeks.org/rearrange-array-arrj-becomes-arri-j/

# A simple Python3 program to rearrange
# contents of arr[] such that arr[j]
# becomes j if arr[i] is j
 
# A simple method to rearrange
# 'arr[0..n-1]' so that 'arr[j]'
# becomes 'i' if 'arr[i]' is 'j'
def rearrange(arr, n):
     
    for i in range(n):
         
        # Retrieving old value and
        # storing with the new one
        arr[arr[i] % n] += i * n
     
    for i in range(n):
         
        # Retrieving new value
        arr[i] //= n
     
# A utility function to pr
# contents of arr[0..n-1]
def printArray(arr, n):
     
    for i in range(n):
        print(arr[i], end = " ")
    print()
 
# Driver code
arr = [2, 0, 1, 4, 5, 3]
n = len(arr)
 
print("Given array is : ")
printArray(arr, n)
 
rearrange(arr, n)
 
print("Modified array is :")
printArray(arr, n)