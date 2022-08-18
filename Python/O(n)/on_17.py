# Python3 implementation of left rotation
# of an array K number of times
 
# Fills temp with two copies of arr
def preprocess(arr, n):
    temp = [None] * (2 * n)
     
    # Store arr elements at i and i + n
    for i in range(n):
        temp[i] = temp[i + n] = arr[i]
    return temp
 
# Function to left rotate an array k times
def leftRotate(arr, n, k, temp):
     
    # Starting position of array after k
    # rotations in temp will be k % n
    start = k % n
     
    # Print array after k rotations
    for i in range(start, start + n):
        print(temp[i], end = " ")
    print("")
 
# Driver program
arr = [1, 3, 5, 7, 9]
n = len(arr)
temp = preprocess(arr, n)
 
k = 2
leftRotate(arr, n, k, temp)
       
k = 3
leftRotate(arr, n, k, temp)
       
k = 4
leftRotate(arr, n, k, temp)