# Python3 program to find the
# count of rotations
  
# Function to return the count 
# of rotations
def countRotation(arr, n):
      
    for i in range (1, n):
          
        # Find the smallest element
        if (arr[i] < arr[i - 1]):
              
            # Return its index
            return i
      
    # If array is not
    # rotated at all
    return 0
  
# Driver Code
if __name__ == "__main__":
      
    arr1 = [ 4, 5, 1, 2, 3 ]
    n = len(arr1)
      
    print(countRotation(arr1, n))