# Python3 program for right rotation of
# an array (Reversal Algorithm)
 
 
# Function to reverse arr
# from index start to end
def reverseArray( arr, start, end):
     
    while (start < end):
         
        arr[start], arr[end] = arr[end], arr[start]
        start = start + 1
        end = end - 1
     
 
# Function to right rotate arr
# of size n by d
def rightRotate( arr, d, n):
     
    reverseArray(arr, 0, n - 1);
    reverseArray(arr, 0, d - 1);
    reverseArray(arr, d, n - 1);
 
 
# function to print an array
def printArray( arr, size):
    for i in range(0, size):
        print (arr[i], end = ' ')
 
 
# Driver code
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
n = len(arr)
k = 3
     
# Function call
rightRotate(arr, k, n)
printArray(arr, n)