# Python3 program for the above approach
from collections import defaultdict
  
# Function to maximize the matching
# pairs between two permutation
# using left and right rotation
def maximumMatchingPairs(perm1, perm2, n):
  
    # Left array store distance of element
    # from left side and right array store
    # distance of element from right side
    left = [0] * n
    right = [0] * n
  
    # Map to store index of elements
    mp1 = {}
    mp2 = {}
    for i in range (n):
        mp1[perm1[i]] = i
      
    for j in range (n):
        mp2[perm2[j]] = j
      
    for i in range (n):
  
        # idx1 is index of element
        # in first permutation
  
        # idx2 is index of element
        # in second permutation
        idx2 = mp2[perm1[i]]
        idx1 = i
  
        if (idx1 == idx2):
  
            # If element if present on same
            # index on both permutations then
            # distance is zero
            left[i] = 0
            right[i] = 0
          
        elif (idx1 < idx2):
  
            # Calculate distance from left
            # and right side
            left[i] = (n - (idx2 - idx1))
            right[i] = (idx2 - idx1)
          
        else :
  
            # Calculate distance from left
            # and right side
            left[i] = (idx1 - idx2)
            right[i] = (n - (idx1 - idx2))
  
    # Maps to store frequencies of elements
    # present in left and right arrays
    freq1 = defaultdict (int)
    freq2 = defaultdict (int)
    for i in range (n):
        freq1[left[i]] += 1
        freq2[right[i]] += 1
  
    ans = 0
  
    for i in range( n):
  
        # Find maximum frequency
        ans = max(ans, max(freq1[left[i]],
                           freq2[right[i]]))
  
    # Return the result
    return ans
  
# Driver Code
if __name__ == "__main__":
      
    # Given permutations P1 and P2
    P1 = [ 5, 4, 3, 2, 1 ]
    P2 = [ 1, 2, 3, 4, 5 ]
    n = len(P1)
  
    # Function Call
    print(maximumMatchingPairs(P1, P2, n))