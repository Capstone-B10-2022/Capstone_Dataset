
# Python3 program for rearrange an
# array such that arr[i] = i.
 
# Function to rearrange an array
# such that arr[i] = i.
 
 
def fix(A, len):
 
    for i in range(0, len):
 
        if (A[i] != -1 and A[i] != i):
            x = A[i]
 
            # check if desired place
            # is not vacate
            while (A[x] != -1 and A[x] != x):
                 
                # store the value from
                # desired place
                y = A[x]
 
                # place the x to its correct
                # position
                A[x] = x
 
                # now y will become x, now
                # search the place for x
                x = y
 
            # place the x to its correct
            # position
            A[x] = x
 
            # check if while loop hasn't
            # set the correct value at A[i]
            if (A[i] != i):
 
                # if not then put -1 at
                # the vacated place
                A[i] = -1
 
 
# Driver code
A = [-1, -1, 6, 1, 9, 3, 2, -1, 4, -1]
 
fix(A, len(A))
 
for i in range(0, len(A)):
    print(A[i], end=' ')
 
# This code is contributed by Saloni1297