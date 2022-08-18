# Python3 implementation of
# left rotation of an array
# K number of times
 
# Function to left rotate
# an array k times
def leftRotate(arr, n, k):
     
    # Print array
    # after k rotations
    for i in range(k, k + n):
        print(str(arr[i % n]),
                   end = " ")
 
# Driver Code
arr = [1, 3, 5, 7, 9]
n = len(arr)
k = 2;
leftRotate(arr, n, k)
print()
 
k = 3;
leftRotate(arr, n, k)
print()
 
k = 4
leftRotate(arr, n, k)
print()