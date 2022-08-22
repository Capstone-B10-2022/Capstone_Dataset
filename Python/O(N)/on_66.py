# Source: https://www.geeksforgeeks.org/segregate-even-odd-numbers-set-3/

# Python3 implementation of the above approach
def arrayEvenAndOdd(arr,  n):
     
    index = 0;
    a = [0 for i in range(n)]
     
    for i in range(n):
        if (arr[i] % 2 == 0):
            a[index] = arr[i]
            ind += 1
 
    for i in range(n):
        if (arr[i] % 2 != 0):
            a[index] = arr[i]
            ind += 1
 
    for i in range(n):
        print(a[i], end = " ")
         
    print()
 
# Driver code
arr = [ 1, 3, 2, 4, 7, 6, 9, 10 ]
n = len(arr)
 
# Function call
arrayEvenAndOdd(arr, n)