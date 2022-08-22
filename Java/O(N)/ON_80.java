// Source: https://www.geeksforgeeks.org/maximum-sum-such-that-no-two-elements-are-adjacent/


// Java code to implement the approach
 
import java.lang.*;
import java.util.*;
 
class ON_80 {
    // Function to return max sum such that
    // no two elements are adjacent
    int findMaxSum(int arr[], int n)
    {
        int incl = arr[0];
        int excl = 0;
        int excl_new;
        int i;
 
        for (i = 1; i < n; i++) {
            // Current max excluding i
            excl_new = Math.max(incl, excl);
 
            // Current max including i
            incl = excl + arr[i];
            excl = excl_new;
        }
 
        // Return max of incl and excl
        return Math.max(incl, excl);
    }
 
    // Driver code
    public static void main(String[] args)
    {
        ON_80 sum = new ON_80();
        int arr[] = new int[] { 5, 5, 10, 100,
                                10, 5 };
        int N = arr.length;
 
        // Function call
        System.out.println(
            sum.findMaxSum(arr, N));
    }
}
