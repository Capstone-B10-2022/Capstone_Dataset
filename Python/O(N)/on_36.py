# Python3 program for the above approach 
  
# Function to left rotate 
def left_rotate(arr):
      
    last = arr[1]; 
    for i in range(3, len(arr), 2):
        arr[i - 2] = arr[i]
          
    arr[len(arr) - 1] = last
  
# Function to right rotate 
def right_rotate(arr):
      
    start = arr[len(arr) - 2] 
    for i in range(len(arr) - 4, -1, -2):
        arr[i + 2] = arr[i]
          
    arr[0] = start
  
# Function to rotate the array 
def rotate(arr):
      
    left_rotate(arr)
    right_rotate(arr) 
    for i in range(len(arr)): 
        print(arr[i], end = " ")
  
# Driver code 
arr = [ 1, 2, 3, 4, 5, 6 ] 
  
rotate(arr); 