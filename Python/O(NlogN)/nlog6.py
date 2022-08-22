
# Python3 code to reorder an array
# according to given indices
def heapify(arr, index, i):
     
    largest = i
     
    # left child in 0 based indexing
    left = 2 * i + 1
     
    # right child in 1 based indexing
    right = 2 * i + 2
     
    global heapSize
 
    # Find largest index from root,
    # left and right child
    if (left < heapSize and
        index[left] > index[largest]):
        largest = left
 
    if (right < heapSize and
        index[right] > index[largest]):
        largest = right
 
    if (largest != i):
         
        # Swap arr whenever index is swapped
        arr[largest], arr[i] = arr[i], arr[largest]
        index[largest], index[i] = index[i], index[largest]
 
        heapify(arr, index, largest)
 
def heapSort(arr, index, n):
     
    # Build heap
    global heapSize
     
    for i in range(int((n - 1) / 2), -1, -1):
        heapify(arr, index, i)
         
    # Swap the largest element of
    # index(first element) with
    # the last element
    for i in range(n - 1, 0, -1):
        index[0], index[i] = index[i], index[0]
         
        # Swap arr whenever index is swapped
        arr[0], arr[i] = arr[i], arr[0]
 
        heapSize -= 1
        heapify(arr, index, 0)
 
# Driver Code
arr = [ 50, 40, 70, 60, 90 ]
index = [ 3, 0, 4, 1, 2 ]
 
n = len(arr)
global heapSize
heapSize = n
heapSort(arr, index, n)
 
print("Reordered array is: ")
print(*arr, sep = ' ')
print("Modified Index array is: ")
print(*index, sep = ' ')
 
# This code is contributed by avanitrachhadiya2155