# Python program for the above approach
 
# Function to rotate the array
def rotate(arr, N):
 
    temp = arr[0]
    for i in range(0, N-1):
        arr[i] = arr[i + 1]
    arr[N - 1] = temp
    return
 
# Function to calculate the
# total score of a rotation
def calculate(arr):
 
    score = 0
    for i in range(0, len(arr)):
        if (arr[i] <= i):
            score = score + 1
 
    return score
 
# Function to find the rotation index k
# that corresponds to the highest score
def bestIndex(nums):
 
    N = len(nums)
    high_score = -1
    min_idx = 0
 
    for i in range(0, N):
        if (i != 0):
           
            # Rotates the array to left
            # by one position.
            rotate(nums, N)
 
        # Stores score of current rotation
        cur_score = calculate(nums)
 
        if (cur_score > high_score):
            min_idx = i
            high_score = cur_score
 
    return min_idx
 
# Driver code
arr = [2, 3, 1, 4, 0]
print(bestIndex(arr))
 
# This code is contributed by Taranpreet