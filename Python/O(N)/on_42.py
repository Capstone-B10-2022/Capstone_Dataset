# Source: https://www.geeksforgeeks.org/rearrange-array-arri/

# Python3 program for rearrange an
# array such that arr[i] = i.
if __name__ == "__main__":
 
    arr = [-1, -1, 6, 1, 9,
           3, 2, -1, 4, -1]
    n = len(arr)
    i = 0
    while i < n:
 
        if (arr[i] >= 0 and arr[i] != i):
            (arr[arr[i]],
             arr[i]) = (arr[i],
                        arr[arr[i]])
        else:
            i += 1
 
    for i in range(n):
        print(arr[i], end=" ")