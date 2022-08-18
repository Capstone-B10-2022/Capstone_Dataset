# Python implementation of left rotation of
# an array K number of times
 
# Function to leftRotate array multiple times
 
 
def leftRotate(arr, n, k):
 
    # To get the starting point of rotated array
    mod = k % n
    s = ""
 
    # Prints the rotated array from start position
    for i in range(n):
        print str(arr[(mod + i) % n]),
    print
    return
 
 
# Driver code
arr = [1, 3, 5, 7, 9]
n = len(arr)
k = 2
 
# Function Call
leftRotate(arr, n, k)
 
k = 3
 
# Function Call
leftRotate(arr, n, k)
 
k = 4
 
# Function Call
leftRotate(arr, n, k)