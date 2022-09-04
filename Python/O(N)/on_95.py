# Source: https://www.geeksforgeeks.org/find-the-minimum-distance-between-two-numbers/

# Python program to Find the minimum
# distance between two numbers
import sys

def minDist(arr, n, x, y) :
	
	# idx1 and idx2 will store indices of
	# x or y and min_dist will store the minimum difference
	idx1=-1; idx2=-1; min_dist = sys.maxsize;
	for i in range(n) :
	# if current element is x then change idx1
	if arr[i]==x :
		idx1=i
		
	# if current element is y then change idx2
	elif arr[i]==y :
		idx2=i
		
	# if x and y both found in array
	# then only find the difference and store it in min_dist
	if idx1!=-1 and idx2!=-1 :
		min_dist=min(min_dist,abs(idx1-idx2));
	
	# if left or right did not found in array
	# then return -1
	if idx1==-1 or idx2==-1 :
		return -1
	# return the minimum distance
	else :
		return min_dist

# Driver code
if __name__ == "__main__" :
	
	arr = [ 3, 5, 4, 2, 6, 5, 6, 6, 5, 4, 8, 3]
	n = len(arr)
	x = 3
	y = 6
	print ("Minimum distance between %d and %d is %d\n"%( x, y,minDist(arr, n, x, y)));

# this code is contributed by aditya942003patil
