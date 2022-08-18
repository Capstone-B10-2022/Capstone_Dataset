# Python3 program to find number
# of rotations in a sorted and
# rotated array.
 
# Returns count of rotations for
# an array which is first sorted
# in ascending order, then rotated
def countRotations(arr, n):
 
    # We basically find index
    # of minimum element
    min = arr[0]
    min_index = 0
    for i in range(0, n):
     
        if (min > arr[i]):
         
            min = arr[i]
            min_index = i
         
    return min_index;
 
 
# Driver code
arr = [15, 18, 2, 3, 6, 12]
n = len(arr)
print(countRotations(arr, n))