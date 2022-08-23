// Searching in Array: https://www.geeksforgeeks.org/introduction-to-arrays/

#include <stdio.h>
#include <stdbool.h>
 
int main()
{
 
    // Creating an integer array
    // named arr of size 10.
    int arr[10] = {0,1,2,3,4,5,6,7,8,9};
    bool flag = false;
    
    for(int i = 1; i<=10; i++)
    {
        if(arr[i] == 2)
        {
            flag = true;
        }
    }
 
}