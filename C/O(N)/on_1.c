// Example Q

// Source: https://www.geeksforgeeks.org/time-complexity-and-space-complexity/#:~:text=Time%20Complexity%3A%20The%20time%20complexity,the%20algorithm%20is%20running%20on.

#include <stdio.h>

int main(){
    int N = 2;
    int count = 0;
    for (int i = N; i > 0; i /= 2)
    for (int j = 0; j < i; j++)
        count++;
}

