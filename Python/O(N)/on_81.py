# Source: https://www.geeksforgeeks.org/range-queries-for-frequencies-of-array-elements/

# Python program to find total 
# count of an element in a range
 
# Returns count of element
# in arr[left-1..right-1]
def findFrequency(arr, n, left, right, element):
 
    count = 0
    for i in range(left - 1, right):
        if (arr[i] == element):
            count += 1
    return count
 
 
# Driver Code
arr = [2, 8, 6, 9, 8, 6, 8, 2, 11]
n = len(arr)
 
# Print frequency of 2 from position 1 to 6
print("Frequency of 2 from 1 to 6 = ",
        findFrequency(arr, n, 1, 6, 2))
 
# Print frequency of 8 from position 4 to 9
print("Frequency of 8 from 4 to 9 = ",
        findFrequency(arr, n, 4, 9, 8))
         
     
# This code is contributed by Anant Agarwal.