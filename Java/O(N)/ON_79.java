// Source: https://www.geeksforgeeks.org/maximum-sum-such-that-no-two-elements-are-adjacent/

/*package whatever //do not write package name here */
import java.io.*;
 
class ON_79
{
 
  // Function to find the maximum sum
  static int findMaxSum(int[] arr, int N)
  {
    // Declare dp array
    int[][] dp = new int[N][2];
    if (N == 1) {
      return arr[0];
    }
 
    // Initialize the values in dp array
    dp[0][0] = 0;
    dp[0][1] = arr[0];
 
    // Loop to find the maximum possible sum
    for (int i = 1; i < N; i++) {
      dp[i][1] = dp[i - 1][0] + arr[i];
      dp[i][0] = Math.max(dp[i - 1][1],
                          dp[i - 1][0]);
    }
 
    // Return the maximum sum
    return Math.max(dp[N - 1][0], dp[N - 1][1]);
  }
 
 
  // Driver Code
  public static void main(String args[])
  {
 
    // Creating the array
    int[] arr = { 5, 5, 10, 100, 10, 5 };
    int N = arr.length;
 
    // Function call
    System.out.println(findMaxSum(arr, N));
  }
}