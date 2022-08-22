# Source: https://www.geeksforgeeks.org/to-find-smallest-and-second-smallest-element-in-an-array/

# Python program to find smallest and second smallest elements
import math
 
def print2Smallest(arr):
 
    # There should be atleast two elements
    arr_size = len(arr)
    if arr_size < 2:
        print ("Invalid Input")
        return
 
    first = second = math.inf
    for i in range(0, arr_size):
 
        # If current element is smaller than first then
        # update both first and second
        if arr[i] < first:
            second = first
            first = arr[i]
 
        # If arr[i] is in between first and second then
        # update second
        elif (arr[i] < second and arr[i] != first):
            second = arr[i];
 
    if (second == math.inf):
        print ("No second smallest element")
    else:
        print ('The smallest element is',first,'and', \
              ' second smallest element is',second)
 
# Driver function to test above function
arr = [12, 13, 1, 10, 34, 1]
print2Smallest(arr)