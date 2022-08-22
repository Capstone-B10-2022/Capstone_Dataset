import java.util.*;

class nlog15{

public static void main(String[] args)
{
	int n, i, j, p, q;
	int a[] = {1, 2, 1, 4, 5, 6, 8, 8};
	n = a.length;
	int []b = new int[n];
	for(i = 0; i < n; i++)
	b[i] = a[i];

	Arrays.sort(b);
	p = 0; q = n - 1;
	for(i = n - 1; i >= 0; i--)
	{
	if(i % 2 != 0)
	{
		a[i] = b[q];
		q--;
	}
	else{
		a[i] = b[p];
		p++;
	}
	}
	for(i = 0; i < n; i++)
	{
	System.out.print(a[i]+" ");
	}
}
}

// This code is contributed by gauravrajput1
