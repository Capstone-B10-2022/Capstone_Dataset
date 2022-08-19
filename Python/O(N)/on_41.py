# Source: https://www.geeksforgeeks.org/rearrange-array-arri/

# Python3 program for rearrange an
# array such that arr[i] = i.
 
# Function to rearrange an array
# such that arr[i] = i.
def fix(A):
    s = set()
     
    # Storing all the values in the Set
    for i in range(len(A)):
        s.add(A[i])
 
    for i in range(len(A)):
       
        # check for item if present in set
        if i in s:
            A[i] = i
        else:
            A[i] = -1
    return A
     
# Driver code
if __name__ == "__main__":
    A = [-1, -1, 6, 1, 9,
          3, 2, -1, 4,-1]
    print(fix(A))