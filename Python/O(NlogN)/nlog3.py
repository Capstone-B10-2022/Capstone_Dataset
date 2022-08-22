
# Python3 program for the above approach
 
# Function to sort the cubes of array
def sortArr(arr, n):
 
    # Make a list of tuples in
    # the form(cube of (num), num)
    arr = [(i * i * i, i) for i in arr];
     
    # Sort the array according to
    # the their respective cubes
    arr.sort()
      
    # Print the array
    for i in range(n):
        print(arr[i][1], end = " ");
 
# Driver Code
if __name__ == "__main__" :
 
    # Given array
    arr = [ 4, -1, 0, -5, 6 ];
    n = len(arr);
 
    # Function Call
    sortArr(arr, n);
 
# This code is contributed by AnkitRai01
# O(nlogn)