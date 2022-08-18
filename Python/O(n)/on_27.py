# Python code for the above approach
 
# Function to find the number of cyclic shifts
def find(arr, N):
    maxele = max(arr)
    left = -1
    right = -1
 
    # Placing left pointer
    # On its correct position
    for i in range(N):
        if (arr[i] == maxele):
            left = i
            break
 
    # Placing right pointer
    # On its correct position
    for i in range(N - 1, -1, -1):
        if (arr[i] == maxele):
            right = i
            break
    ans = (N // 2) - (right - left)
    if (ans <= 0):
        return 0
    else:
        return ans
 
# Driver Code
arr = [3, 3, 5, 3, 3, 3]
N = len(arr)
 
# Function call
print(find(arr, N))