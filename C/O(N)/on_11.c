// C program to find minimum element in a sorted and rotated
// array
#include <stdio.h>
 
int findMin(int arr[],int N)
{
       int min_ele = arr[0];
       for(int i=0;i<N;i++){
              if(arr[i]<min_ele){
                     min_ele = arr[i];
              }
       }
       return min_ele;
}
 
// Driver program to test above functions
int main()
{
    int arr1[] = { 5, 6, 1, 2, 3, 4 };
    //int n1 = sizeof(arr1) / sizeof(arr1[0]);
    printf("The minimum element is %d\n",
           findMin(arr1, 6));

 
    return 0;
}