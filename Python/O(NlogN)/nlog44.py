#https://www.geeksforgeeks.org/print-distinct-elements-given-integer-array/
ar = [ 10, 5, 3, 4, 3, 5, 6 ];
hm = {};
for i in range(len(ar)):
	hm[ar[i]] = i;

# Using hm.keySet() to print output
# reduces time complexity. - Lokesh
print(hm.keys());

# This code contributed by shikhasingrajput
