# Source: https://www.geeksforgeeks.org/double-first-element-move-zero-end/


# Maintain last index with positive value
def shiftAllZeroToLeft(arr, n):
    lastSeenNonZero = 0
    for index in range(0, n):
       
        # If Element is non-zero
        if (array[index] != 0):
           
            # swap current index, with lastSeen
            # non-zero
            array[index], array[lastSeenNonZero] = array[lastSeenNonZero], array[index]
             
            # next element will be last seen non-zero
            lastSeenNonZero++