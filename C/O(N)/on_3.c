// Print all elements of the array

#include <stdio.h>

void printAllElementOfArray(int arr[], int size)
{
    for (int i = 0; i < size; i++)
    {
        printf("%d\n", arr[i]);
    }
}

int main(){
    int newarr[] = {1,2,3,4,5};
    int size = (sizeof(newarr)/sizeof(newarr[0]));
    printAllElementOfArray(newarr, size);
}