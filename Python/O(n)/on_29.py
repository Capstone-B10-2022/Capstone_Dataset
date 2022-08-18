# Python3 program to implement
# the above approach
import sys
 
# Function to find the longest subsequence
# having equal left and right rotation
def findAltSubSeq(s):
     
    # Length of the string
    n = len(s)
    ans = -sys.maxsize - 1
     
    # Iterate for all possible combinations
    # of a two-digit numbers
    for i in range(10):
        for j in range(10):
            cur, f = 0, 0
             
            # Check for alternate occurrence
            # of current combination
            for k in range(n):
                if (f == 0 and ord(s[k]) -
                               ord('0') == i):
                    f = 1
                     
                    # Increment the current value
                    cur += 1
                 
                elif (f == 1 and ord(s[k]) -
                                 ord('0') == j):
                    f = 0
                     
                    # Increment the current value
                    cur += 1
             
            # If alternating sequence is
            # obtained of odd length
            if i != j and cur % 2 == 1:
                 
                # Reduce to even length
                cur -= 1
                 
            # Update answer to store
            # the maximum
            ans = max(cur, ans)
             
    # Return the answer
    return ans
 
# Driver code
s = "100210601"
 
print(findAltSubSeq(s))