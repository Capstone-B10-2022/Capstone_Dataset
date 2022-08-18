# Python3 code to implement the approach
 
# Function to find maximum possible product
def findMax(S) :
 
    N = len(S);
    f = ord(S[0]) - ord('0');
    l = ord(S[N - 1]) - ord('0');
 
    Max = f * l;
 
    for i in range(1, N) :
        f = ord(S[i]) - ord('0');
        l = ord(S[i - 1]) - ord('0');
        Max = max(Max, f * l);
 
    # Return the maximum product as the answer
    return Max;
 
# Driver Code
if __name__ == "__main__" :
 
    Str = "12345";
 
    # Function Call
    print(findMax(Str));