# Python3 implementation to check
# that the given string can be
# converted to another string 
# by circular clockwise shift
  
# Function to check that the 
# string s1 can be converted
# to s2 by clockwise circular
# shift of all characters of 
# str1 atmost X times
def isConversionPossible(s1, s2, x):
    n = len(s1)
    s1 = list(s1)
    s2 = list(s2)
      
    for i in range(n):
          
        # Difference between the 
        # ASCII numbers of characters
        diff = ord(s2[i]) - ord(s1[i])
          
        # If both characters 
        # are the same
        if diff == 0:
            continue
          
        # Condition to check if the 
        # difference less than 0 then
        # find the circular shift by 
        # adding 26 to it
        if diff < 0:
            diff = diff + 26
        # If difference between 
        # their ASCII values
        # exceeds X
        if diff > x:
            return False
      
    return True
      
  
# Driver Code
if __name__ == "__main__":
    s1 = "you"
    s2 = "ara"
    x = 6
      
    # Function Call
    result = isConversionPossible(s1, s2, x)
      
    if result:
        print("YES")
    else:
        print("NO")