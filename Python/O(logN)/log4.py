# Function to find the cross over point
# (the point before which elements are
# smaller than or equal to x and after
# which greater than x)
def findCrossOver(arr, low, high, x) :
 
    # Base cases
    if (arr[high] <= x) : # x is greater than all
        return high
         
    if (arr[low] > x) : # x is smaller than all
        return low
     
    # Find the middle point
    mid = (low + high) // 2 # low + (high - low)// 2
     
    # If x is same as middle element,
    # then return mid
    if (arr[mid] <= x and arr[mid + 1] > x) :
        return mid
     
    # If x is greater than arr[mid], then
    # either arr[mid + 1] is ceiling of x
    # or ceiling lies in arr[mid+1...high]
    if(arr[mid] < x) :
        return findCrossOver(arr, mid + 1, high, x)
     
    return findCrossOver(arr, low, mid - 1, x)
 
# This function prints k closest elements to x
# in arr[]. n is the number of elements in arr[]
def printKclosest(arr, x, k, n) :
     
    # Find the crossover point
    l = findCrossOver(arr, 0, n - 1, x)
    r = l + 1 # Right index to search
    count = 0 # To keep track of count of
              # elements already printed
 
    # If x is present in arr[], then reduce
    # left index. Assumption: all elements
    # in arr[] are distinct
    if (arr[l] == x) :
        l -= 1
 
    # Compare elements on left and right of crossover
    # point to find the k closest elements
    while (l >= 0 and r < n and count < k) :
         
        if (x - arr[l] < arr[r] - x) :
            print(arr[l], end = " ")
            l -= 1
        else :
            print(arr[r], end = " ")
            r += 1
        count += 1
 
    # If there are no more elements on right
    # side, then print left elements
    while (count < k and l >= 0) :
        print(arr[l], end = " ")
        l -= 1
        count += 1
 
    # If there are no more elements on left
    # side, then print right elements
    while (count < k and r < n) :
        print(arr[r], end = " ")
        r += 1
        count += 1
 
# Driver Code
if __name__ == "__main__" :
 
    arr =[12, 16, 22, 30, 35, 39, 42,
              45, 48, 50, 53, 55, 56]
                 
    n = len(arr)
    x = 35
    k = 4
     
    printKclosest(arr, x, 4, n)
     
# This code is contributed by Ryuga
# O(logn +K)