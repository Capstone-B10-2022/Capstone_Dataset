# Source: https://www.geeksforgeeks.org/find-elements-array-least-two-greater-elements/

# Python3 program to find all elements
# in array which have atleast two
# greater elements itself.
import sys
 
def findElements(arr, n):
 
    first = -sys.maxsize
    second = -sys.maxsize
 
    for i in range(0, n):
     
        # If current element is smaller
        # than first then update both
        # first and second
        if (arr[i] > first):
         
            second = first
            first = arr[i]
         
        # If arr[i] is in between first
        # and second then update second
        elif (arr[i] > second):
            second = arr[i]
     
    for i in range(0, n):
        if (arr[i] < second):
            print(arr[i], end =" ")
 
 
# Driver code
arr = [2, -6, 3, 5, 1]
n = len(arr)
findElements(arr, n)