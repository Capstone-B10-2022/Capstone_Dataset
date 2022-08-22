# Source: https://www.geeksforgeeks.org/program-for-mean-and-median-of-an-unsorted-array/

# Python3 program to find mean
 
# Function for calculating mean
 
 
def findMean(a, n):
 
    sum = 0
    for i in range(0, n):
        sum += a[i]
 
    return float(sum/n)
 
 
# Driver code
a = [1, 3, 4, 2, 7, 5, 8, 6]
n = len(a)
 
# Function call
print("Mean =", findMean(a, n))