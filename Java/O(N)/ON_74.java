// Source: https://www.geeksforgeeks.org/program-for-mean-and-median-of-an-unsorted-array/

// Java program to find mean
// and median of an array
import java.util.*;
 
class ON_74
{
    // Function for calculating mean
    public static double findMean(int a[], int n)
    {
        int sum = 0;
        for (int i = 0; i < n; i++)
            sum += a[i];
 
        return (double)sum / (double)n;
    }
 
    // Driver code
    public static void main(String args[])
    {
        int a[] = { 1, 3, 4, 2, 7, 5, 8, 6 };
        int n = a.length;
       
        // Function call
        System.out.println("Mean = " + findMean(a, n));
    }
}
