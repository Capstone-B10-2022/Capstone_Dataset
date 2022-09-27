// Source: https://www.geeksforgeeks.org/java-program-for-minimum-move-to-end-operations-to-make-all-strings-equal/
// Java program to make all
// strings same using move
// to end operations.
import java.util.*;
class ON3_1
{
 
// Returns minimum number of
// moves to end operations
// to make all strings same.
static int minimunMoves(String arr[], int n)
{
    int ans = Integer.MAX_VALUE;
    for (int i = 0; i < n; i++)
    {
        int curr_count = 0;
 
        // Consider s[i] as target
        // string and count rotations
        // required to make all other
        // strings same as str[i].
        String tmp = "";
        for (int j = 0; j < n; j++)
        {
            tmp = arr[j] + arr[j];
 
            // find function returns the
            // index where we found arr[i]
            // which is actually count of
            // move-to-front operations.
            int index = tmp.indexOf(arr[i]);
 
            // If any two strings are not
            // rotations of each other,
            // we can't make them same.
            if (index == arr[i].length())
                return -1;
                 
            curr_count += index;
        }
 
        ans = Math.min(curr_count, ans);
    }
 
    return ans;
}
 
// Driver code
public static void main(String args[])
{
    String arr[] = {"xzzwo", "zwoxz",
                    "zzwox", "xzzwo"};
    int n = arr.length;
    System.out.println(minimunMoves(arr, n));
}
}
