# Python code for the above approach
 
# Function to rotate the array
# to the right, K times
def RightRotate(nums, K) :
    n = len(nums)
 
    # Case when K > N or K < -N
    K = ((K * -1) % n) * -1 if K < 0 else K % n;
 
    # Case when K is negative
    K = (n - (K * -1)) if K < 0 else K;
 
    # Reverse all the array elements
    nums.reverse();
 
    # Reverse the first k elements
    p1 = nums[0:K]
    p1.reverse();
 
    # Reverse the elements from K
    # till the end of the array
    p2 = nums[K:]
    p2.reverse();
    arr = p1 + p2
 
    return arr;
 
# Driver code
 
# Initialize the array
Array = [1, 2, 3, 4, 5];
 
# Find the size of the array
N = len(Array)
 
# Initialize K
K = -2;
 
# Call the function and
# print the answer
Array = RightRotate(Array, K);
 
# Print the array after rotation
for i in Array:
    print(i, end=" ")