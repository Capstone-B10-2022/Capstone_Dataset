# Python 3 program to make all strings
# same using move to end operations.
import sys
 
# Returns minimum number of moves to end
# operations to make all strings same.
def minimunMoves(arr, n):
 
    ans = sys.maxsize
    for i in range(n):
 
        curr_count = 0
 
        # Consider s[i] as target string and
        # count rotations required to make
        # all other strings same as str[i].
        for j in range(n):
 
            tmp = arr[j] + arr[j]
 
            # find function returns the index where
            # we found arr[i] which is actually
            # count of move-to-front operations.
            index = tmp.find(arr[i])
 
            # If any two strings are not rotations of
            # each other, we can't make them same.
            if (index == len(arr[i])):
                return -1
 
            curr_count += index
 
        ans = min(curr_count, ans)
 
    return ans
 
# Driver Code
if __name__ == "__main__":
     
    arr = ["xzzwo", "zwoxz", "zzwox", "xzzwo"]
    n = len(arr)
    print( minimunMoves(arr, n))