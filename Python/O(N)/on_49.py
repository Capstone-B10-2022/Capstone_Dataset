# Source: https://www.geeksforgeeks.org/rearrange-array-such-that-even-positioned-are-greater-than-odd/

# Python3 program to rearrange
# the elements in the array
# such that even positioned are
# greater than odd positioned elements
def rearrange(arr, n):
 
    for i in range (1, n):
       
        # if index is even
        if (i % 2 == 0):
            if (arr[i] > arr[i - 1]):
                arr[i - 1], arr[i] = arr[i], arr[i - 1]
         
        # if index is odd
        else:
            if (arr[i] < arr[i - 1]):
                arr[i - 1], arr[i] = arr[i] , arr[i - 1]
 
if __name__ == "__main__":         
    n = 5
    arr = [1, 3, 2, 2, 5]
    rearrange(arr, n);
    for i in range (n):
        print (arr[i], end = " ")
    print ()