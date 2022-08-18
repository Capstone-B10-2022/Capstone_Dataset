# Python3 program to split array and
# move first part to end.
 
# Function to split array and
# move first part to end
def SplitAndAdd(A, length, rotation):
 
    # make a temporary array with double
    # the size and each index is initialized to 0
    tmp = [ 0 for i in range(length * 2)]
 
    # copy array element in to new array twice
    for i in range(length):
        tmp[i] = A[i]
        tmp[i + length] = A[i]
 
    for i in range(rotation,
                   rotation + length, 1):
        A[i - rotation] = tmp[i];
      
# Driver code
arr = [12, 10, 5, 6, 52, 36]
n = len(arr)
position = 2
SplitAndAdd(arr, n, position);
for i in range(n):
    print(arr[i], end = " ")
print()