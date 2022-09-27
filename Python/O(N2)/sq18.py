# Python3 program for above approach
 
# Function to transform the array
def fixArray(ar, n):
     
    # Iterate over the array
    for i in range(n):
        for j in range(n):
 
            # Check is any ar[j]
            # exists such that
            # ar[j] is equal to i
            if (ar[j] == i):
                ar[j], ar[i] = ar[i], ar[j]
 
    # Iterate over array
    for i in range(n):
         
        # If not present
        if (ar[i] != i):
            ar[i] = -1
 
    # Print the output
    print("Array after Rearranging")
 
    for i in range(n):
        print(ar[i], end = " ")
 
# Driver Code
ar = [ -1, -1, 6, 1, 9, 3, 2, -1, 4, -1 ]
n = len(ar)
 
# Function Call
fixArray(ar, n);
 
# This code is contributed by rag2127