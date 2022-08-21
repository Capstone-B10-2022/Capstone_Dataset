# Source: https://www.geeksforgeeks.org/rearrange-array-even-index-elements-smaller-odd-index-elements-greater/

# Python code to rearrange
# an array such that
# even index elements
# are smaller and odd
# index elements are
# greater than their
# next.
 
def rearrange(arr, n):
 
    for i in range(n - 1):
        if (i % 2 == 0 and arr[i] > arr[i + 1]):
         
            temp = arr[i]
            arr[i]= arr[i + 1]
            arr[i + 1]= temp
         
        if (i % 2 != 0 and arr[i] < arr[i + 1]):
          
            temp = arr[i]
            arr[i]= arr[i + 1]
            arr[i + 1]= temp
            
  
# Utility that prints out an array in
# a line
def printArray(arr, size):
 
    for i in range(size):
        print(arr[i], " ", end ="")
  
    print()
 
# Driver code
 
arr = [ 6, 4, 2, 1, 8, 3 ]
n = len(arr)
  
print("Before rearranging: ")
printArray(arr, n)
  
rearrange(arr, n)
  
print("After rearranging:")
printArray(arr, n);