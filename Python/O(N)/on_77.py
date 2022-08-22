# Source: https://www.geeksforgeeks.org/maximum-sum-such-that-no-two-elements-are-adjacent/

# Python code to implement the approach
 
# Function to return max sum such that
# no two elements are adjacent
def findMaxSum(arr, n):
    incl = 0
    excl = 0  
    for i in arr:
         
        # Current max excluding i
        new_excl = max (excl, incl)
         
        # Current max including i
        incl = excl + i
        excl = new_excl
     
    # Return max of incl and excl
    return max(excl, incl)
 
# Driver code
if __name__ == "__main__":
    arr = [5, 5, 10, 100, 10, 5]
    N = 6
     
    # Function call
    print (findMaxSum(arr, N))