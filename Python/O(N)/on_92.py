# Source: https://www.geeksforgeeks.org/maximum-profit-by-buying-and-selling-a-share-at-most-twice/

import sys

def maxtwobuysell(arr, size):
	first_buy = -sys.maxsize;
	first_sell = 0;
	second_buy = -sys.maxsize;
	second_sell = 0;

	for i in range(size):

		first_buy = max(first_buy, -arr[i]);
		first_sell = max(first_sell, first_buy + arr[i]);
		second_buy = max(second_buy, first_sell - arr[i]);
		second_sell = max(second_sell, second_buy + arr[i]);

	
	return second_sell;

if __name__ == '__main__':
	arr = [ 2, 30, 15, 10, 8, 25, 80 ];
	size = len(arr);
	print(maxtwobuysell(arr, size));

# This code is contributed by gauravrajput1
