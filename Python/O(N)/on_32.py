# Python3 program for the above approach
  
# Function that prints maximum
# equal elements
def maximumEqual(a, b, n):
  
    # List to store the index
    # of elements of array b
    store = [0] * 10 ** 5
      
    # Storing the positions of
    # array B
    for i in range(n):
        store[b[i]] = i + 1
  
    # Frequency array to keep count
    # of elements with similar
    # difference in distances 
    ans = [0] * 10 ** 5
  
    # Iterate through all element 
    # in arr1[]
    for i in range(n):
  
        # Calculate number of shift 
        # required to make current 
        # element equal
        d = abs(store[a[i]] - (i + 1))
  
        # If d is less than 0
        if (store[a[i]] < i + 1):
            d = n - d
  
        # Store the frequency
        # of current diff
        ans[d] += 1
          
    finalans = 0
  
    # Compute the maximum frequency
    # stored
    for i in range(10 ** 5):
        finalans = max(finalans, ans[i])
  
    # Printing the maximum number
    # of equal elements
    print(finalans)
  
# Driver Code
if __name__ == '__main__':
  
    # Given two arrays
    A = [ 6, 7, 3, 9, 5 ]
    B = [ 7, 3, 9, 5, 6 ]
  
    size = len(A)
  
    # Function Call
    maximumEqual(A, B, size)