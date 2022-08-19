# Python program to implement
# the above approach
 
# Function to find the minimum number
# of steps
def findMinimumNumberOfSteps(arr, K) :
 
    # Variable to store the answer
    time = 0
 
    # Traverse in the while loop
    while (arr[K] != 0) :
 
        # Iterate over the loop
        for i in range(0, len(arr)) :
             
            # Check the condition and
            # decrease the value
            if (arr[i] > 0) :
                arr[i] -= 1
                time += 1
             
 
            # Break the loop
            if (arr[K] == 0):
                break
 
    # Print the result
    print(time)
 
# Driver Code
arr = [ 2, 3, 2 ]
K = 2
findMinimumNumberOfSteps(arr, K)