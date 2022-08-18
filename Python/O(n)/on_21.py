# Python Program to solve queries on Left and Right
# Circular shift on array
 
# Function to solve query of type 1 x.
def querytype1(toRotate, times, n):
   
    # Decreasing the absolute rotation
    toRotate = (toRotate - times) % n
    return toRotate
 
# Function to solve query of type 2 y.
def querytype2(toRotate, times, n):
   
    # Increasing the absolute rotation.
    toRotate = (toRotate + times) % n
    return toRotate
 
# Function to solve queries of type 3 l r.
def querytype3( toRotate, l, r, preSum, n):
   
    # Finding absolute l and r.
    l = (l + toRotate + n) % n
    r = (r + toRotate + n) % n
 
    # if l is before r.
    if (l <= r):
        print((preSum[r + 1] - preSum[l]))  
 
    # If r is before l.
    else:
        print((preSum[n] + preSum[r + 1] - preSum[l]))
 
# Wrapper Function solve all queries.
def wrapper( a, n):
    preSum = [ 0 for i in range(n + 1)]
     
    # Finding Prefix sum
    for i in range(1,n+1):
        preSum[i] = preSum[i - 1] + a[i - 1]
 
    toRotate = 0
 
    # Solving each query
    toRotate = querytype1(toRotate, 3, n)
    querytype3(toRotate, 0, 2, preSum, n)
    toRotate = querytype2(toRotate, 1, n)
    querytype3(toRotate, 1, 4, preSum, n);
 
# Driver Program
if __name__ == '__main__':
    arr = [ 1, 2, 3, 4, 5 ]
    N = len(arr)
    wrapper(arr, N)