
# Python3 code for above implementation
  
def leftRotate(arr, d, n): 
    if(d == 0 or d == n): 
        return; 
    i = d 
    j = n - d 
    while (i != j): 
          
        if(i < j): # A is shorter
            swap(arr, d - i, d + j - i, i) 
            j -= i 
          
        else: # B is shorter
            swap(arr, d - i, d, j) 
            i -= j 
      
    swap(arr, d - i, d, i)