# Python3 program to find maximum sum of
# all rotation of i*arr[i] using pivot.
 
# function definition
def maxSum(arr, n) :
 
    sum = 0
    pivot = findPivot(arr, n)
 
    # difference in pivot and index
    # of last element of array
    diff = n - 1 - pivot
    for i in range(n) :
        sum = sum + ((i + diff) % n) * arr[i];
     
    return sum
     
# function to find pivot
def findPivot(arr, n) :
    for i in range(n) :
 
        if(arr[i] > arr[(i + 1) % n]) :
            return i;
 
# Driver code
if __name__ == "__main__" :
 
    # rotated input array
    arr = [8, 3, 1, 2]
    n= len(arr)
     
    max= maxSum(arr, n)
    print(max)