
#include <stdio.h>
 
void swap(int *x, int *y)
{
  int temp = *x;
  *x = *y;
  *y = temp;
}
void rotate(int arr[], int n)
{
  int i = 0, j = n - 1;
  while(i != j)
  {
    swap(&arr[i], &arr[j]);
    i++;
  }
}
 
int main()
{
    int arr[] = {1, 2, 3, 4, 5}, i;
    int n = sizeof(arr)/sizeof(arr[0]);
 
    printf("Given array is\n");
    for (i = 0; i < n; i++)
        printf("%d ", arr[i]);
 
    rotate(arr, n);
 
    printf("\nRotated array is\n");
    for (i = 0; i < n; i++)
        printf("%d ", arr[i]);
 
    return 0;
}