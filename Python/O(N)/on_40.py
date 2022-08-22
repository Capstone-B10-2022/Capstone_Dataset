# Python program of the above approach
 
# Utility function to rotate the digits of
# array elements such that array elements are
# in placed even-odd or odd-even alternately
def is_possible(arr, check):
 
    # Checks if array can be converted
    # into even-odd or odd-even form
    exists = True
 
    # Store array elements
    cpy = arr
 
    # Traverse the array
    for i in range(len(arr)):
 
        # Check if arr[i] is already
        # at correct position
        if (arr[i] % 2 == check):
            check = not(check)
            continue
 
        # Checks if it is possible
        # to modify the number arr[i]
        # by rotating the digits of
        # the number anticlockwise
        flag = False
 
        # Stores the number arr[i] as
        # string
        strEle = str(arr[i])
 
        # Traverse over the digits of
        # the current element
        for j in range(len(strEle)):
 
            # Checks if parity of check and
            # current digit is same or not
            if int(strEle[j]) % 2 == check:
 
                # Rotates the string by j + 1 times
                # in anticlockwise
                arr[i] = int(strEle[j + 1:] + strEle[:j + 1])
 
                # Marks the flag
                # as true and break
                flag = True
                break
 
        # If flag is false
        if flag == False:
 
            # Update exists
            exists = False
            break
 
        # Changes the
        # parity of check
        check = not(check)
 
    # Checks if arr[] cannot be
    # modified, then returns false
    if not exists:
        arr = cpy
        return False
         
         
    # Otherwise, return True
    else:
        return True
 
# Function to rotate the digits of array
# elements such that array elements are
# in the form of even-odd or odd-even form
def convert_arr(arr):
 
    # If array elements can be arranged
    # in even-odd manner alternately
    if(is_possible(arr, 0)):
        print(*arr)
 
    # If array elements can be arranged
    # in odd-even manner alternately
    elif(is_possible(arr, 1)):
        print(*arr)
         
    # Otherwise, prints -1
    else:
        print(-1)
 
# Driver Code
if __name__ == '__main__':
     
    arr = [143, 251, 534, 232, 854]
    convert_arr(arr)