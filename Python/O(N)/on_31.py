# Python3 program to implement the
# above approach
  
# Function to return the
# count of rotations
def countRotation(arr, low, high):
  
    # If array is not rotated
    if (low > high):
        return 0
  
    mid = low + (high - low) // 2
  
    # Check if current element is
    # greater than the next
    # element
    if (mid < high and arr[mid] > arr[mid + 1]):
  
        # The next element is
        # the smallest
        return mid + 1
  
    # Check if current element is
    # smaller than it's previous
    # element
    if (mid > low and arr[mid] < arr[mid - 1]):
  
        # Current element is
        # the smallest
        return mid
  
    # Check if current element is
    # greater than lower bound
    if (arr[mid] > arr[low]):
  
        # The sequence is increasing
        # so far
        # Search for smallest
        # element on the right
        # subarray
        return countRotation(arr, mid + 1, high)
  
    if (arr[mid] < arr[high]):
  
        # Smallest element lies on the
        # left subarray
        return countRotation(arr, low, mid - 1)
  
    else:
  
        # Search for the smallest
        # element on both subarrays
        rightIndex = countRotation(arr, 
                                mid + 1,
                                high)
        leftIndex = countRotation(arr, low,
                                mid - 1)
          
        if (rightIndex == 0):
            return leftIndex
  
        return rightIndex
  
# Driver code
if __name__ == '__main__':
      
    arr1 = [ 4, 5, 1, 2, 3 ]
    N = len(arr1)
  
    print(countRotation(arr1, 0, N - 1))