# Python program for above approach
 
# Function to find no of iterations.
def minZero(A, n):
 
    # Initialize count c = 0.
    c = 0
 
    # if zero is already present
    # in array return c.
    if min(A) == 0:
        return c
 
    # Iterate till minimum
    # in array becomes zero.
    while min(A) != 0:
 
        # Copy array element to A1
        A1 = A[:]
 
        # Pop first element and
        # append it to last
        x = A.pop(0)
        A.append(x)
 
        # Perform subtraction
        for i in range(n):
            A[i] = abs(A[i]-A1[i])
 
        # Increment count by 1
        c += 1
 
    # Return value of count c
    return c
 
# Driver Code
 
# Original array
arr = [2, 6, 3, 4, 8, 7]
 
# Calling method minZero
x = minZero(arr, len(arr))
 
# Print the result
print(x)