# Python program to print
# all possible rotations
# of the given array
 
# Function to reverse array
# between indices s and e
def reverse(arr, s, e):
    while s < e:
        tem = arr[s]
        arr[s] = arr[e]
        arr[e] = tem
        s = s + 1
        e = e - 1
# Function to generate all
# possible rotations of array
def fun(arr, k):
    n = len(arr)-1
    # k = k % n
    v = n - k
    if v>= 0:
        reverse(arr, 0, v)
        reverse(arr, v + 1, n)
        reverse(arr, 0, n)
        return arr
# Driver Code
arr = [1, 2, 3, 4]
for i in range(0, len(arr)):
    count = 0
    p = fun(arr, i)
    print(p, end =" ")