# Source: https://www.geeksforgeeks.org/to-find-smallest-and-second-smallest-element-in-an-array/


# python program to find smallest and second smallest element in array
 
# import the module
import sys
 
arr = [12, 13, 1, 10, 34, 1]
n = len(arr)
smallest = sys.maxint
 
# traversing the array to find smallest element.
for i in range(n):
    if(arr[i] < smallest):
        smallest = arr[i]
 
print('smallest element is: ' + str(smallest))
second_smallest = sys.maxint
 
# traversing the array to find second smallest element
for i in range(n):
    if(arr[i] < second_smallest and arr[i] > smallest):
        second_smallest = arr[i]
 
print('second smallest element is: ' + str(second_smallest))