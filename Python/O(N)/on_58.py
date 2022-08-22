# Source: https://www.geeksforgeeks.org/rearrange-array-maximum-minimum-form-set-2-o1-extra-space/


# Python 3 program to rearrange an
# array in minimum maximum form
 
# Prints max at first position, min
# at second position second max at
# third position, second min at
# fourth position and so on.
def rearrange(arr, n):
 
    # initialize index of first minimum
    # and first maximum element
    max_ele = arr[n - 1]
    min_ele = arr[0]
 
    # traverse array elements
    for i in range(n):
         
        # at even index : we have to
        # put maximum element
        if i % 2 == 0:
            arr[i] = max_ele
            max_ele -= 1
 
        # at odd index : we have to
        # put minimum element
        else:
            arr[i] = min_ele
            min_ele += 1
 
# Driver code
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
n = len(arr)
print("Original Array")
for i in range(n):
    print(arr[i], end = " ")
 
rearrange(arr, n)
print("\nModified Array")
for i in range(n):
    print(arr[i], end = " ")