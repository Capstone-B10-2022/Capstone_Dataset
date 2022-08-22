if __name__ == '__main__':
    	#n, i, j, p, q;
	a = [ 1, 2, 1, 4, 5, 6, 8, 8 ];
	n = len(a);
	b = [0]*n;
	for i in range(n):
		b[i] = a[i];

	b.sort();
	p = 0;
	q = n - 1;
	for i in range(n-1, -1,-1):
		if (i % 2 != 0):
			a[i] = b[q];
			q -= 1;
		else:
			a[i] = b[p];
			p += 1;
		
	for i in range(n):
		print(a[i], end=" ");
	
# This code is contributed by gauravrajput1
