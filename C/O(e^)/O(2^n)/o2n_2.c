// Source: https://www.geeksforgeeks.org/recursion/
// Write a program and recurrence relation to find the Factorial of n where n>2 . 

// C code to implement factorial
#include <stdio.h>
 
// Factorial function
int f(int n)
{
    // Stop condition
    if (n == 0 || n == 1)
        return 1;
 
    // Recursive condition
    else
        return n * f(n - 1);
}
 
// Driver code
int main()
{
    int n = 5;
    printf("factorial of %d is: %d", n, f(n));
    return 0;
}