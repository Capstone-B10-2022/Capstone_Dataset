# python3 program for above approach
 
# Function to check if two matrices
# are equal or not
def isEqual(arr, brr):
    n = len(arr)
    m = len(arr[0])
 
    for i in range(0, n):
        for j in range(0, m):
            if (arr[i][j] != brr[i][j]):
                return False
 
    return True
 
# Function to rotate matrix by 90 degrees clockwise
def rotate(m):
    n = len(m)
 
    for i in range(0, n):
        for j in range(0, i):
            temp = m[i][j]
            m[i][j] = m[j][i]
            m[j][i] = temp
 
    for i in range(0, n):
        m[i].reverse()
 
# Find Minimum rotation to reach the desired matrix
def findRotation(arr, brr):
    if (isEqual(arr, brr)):
        print(0)
        return
 
    for i in range(1, 4):
 
        # Rotate by 90 degrees clockwise
        rotate(arr)
 
        # Checking if both arr[][] and brr[]
        # are now equal or not
        if (isEqual(arr, brr)):
            if (i < 4 - i):
                print(f"+{i}")
 
            else:
                print(f"-{4-i}")
            return
 
    # If converting brr[][] is not possible
    print("NA")
 
# Driver Code
if __name__ == "__main__":
 
    arr = [[2, 3], [4, 5]]
    brr = [[4, 2], [5, 3]]
 
    # Function Call
    findRotation(arr, brr)