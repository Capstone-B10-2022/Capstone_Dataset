//Java code for above implementation
static void ON_11(int arr[], int d, int n) 
{ 
int i, j; 
if(d == 0 || d == n) 
    return; 
/* If number of elements to be rotated is more than array size*/ 
if(d > n)
   d = d % n;
i = d; 
j = n - d; 
while (i != j) 
{ 
    if(i < j) /*A is shorter*/
    { 
    swap(arr, d-i, d+j-i, i); 
    j -= i; 
    } 
    else /*B is shorter*/
    { 
    swap(arr, d-i, d, j); 
    i -= j; 
    } 
    // printArray(arr, 7); 
} 
/*Finally, block swap A and B*/
swap(arr, d-i, d, i); 
}