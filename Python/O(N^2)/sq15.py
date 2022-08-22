# Python3 code to Find another array
# such that the hamming distance
# from the original array is maximum
 
# Return the maximum hamming
# distance of a rotation
def maxHamming( arr , n ):
 
    # arr[] to brr[] two times so
    # that we can traverse through
    # all rotations.
    brr = [0] * (2 * n + 1)
    for i in range(n):
        brr[i] = arr[i]
    for i in range(n):
        brr[n+i] = arr[i]
     
    # We know hamming distance
    # with 0 rotation would be 0.
    maxHam = 0
     
    # We try other rotations one by
    # one and compute Hamming
    # distance of every rotation
    for i in range(1, n):
        currHam = 0
        k = 0
        for j in range(i, i + n):
            if brr[j] != arr[k]:
                currHam += 1
                k = k + 1
         
        # We can never get more than n.
        if currHam == n:
            return n
         
        maxHam = max(maxHam, currHam)
     
    return maxHam
 
# driver program
arr = [2, 4, 6, 8]
n = len(arr)
print(maxHamming(arr, n))
 
# This code is contributed by "Sharad_Bhardwaj".