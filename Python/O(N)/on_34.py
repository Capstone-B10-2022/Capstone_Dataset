# Python program for above approach
 
# Function to find no of iterations
def minZero(A, n):
 
    # Initialize count c = 0
    c = 0
 
    # If 0 already in array return c
    if min(A) == 0:
        return c
 
    # Iterate till we get zero in array
    while min(A) != 0:
 
        # Assign first element in x
        x = A[0]
 
        # Loop to subtract consecutive element
        for i in range(n-1):
            A[i] = abs(A[i]-A[i + 1])
        A[n-1] = abs(A[n-1]-x)
 
        # Increment count c
        c += 1
 
    # Return c
    return c
 
# Driver Code
 
# Original array
arr = [2, 6, 3, 4, 8, 7]
 
# Length of array
N = len(arr)
 
# calling function
x = minZero(arr, N)
 
# print the result
print(x)