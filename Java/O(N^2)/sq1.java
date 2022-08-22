// Java code to implement the above approach
import java.util.*;
 
class sq1 {
 
 
  // After transpose we swap
  // elements of column
  // one by one for finding left
  // rotation of matrix
  // by 90 degree
  static void reverseColumns(int[][] arr)
  {
    int R = arr.length;
    int C = arr[0].length;
 
    for (int i = 0; i < C; i++){
      for (int j = 0, k = C - 1; j < k; j++, k--){
        int temp = arr[j][i];
        arr[j][i] = arr[k][i];
        arr[k][i] = temp;
      }
    }
  }
 
  // Function to do transpose of matrix
  static void transpose(int[][] arr)
  {
    int R = arr.length;
    int C = arr[0].length;
 
    for (int i = 0; i < R; i++){
      for (int j = i; j < C; j++){
        int temp = arr[j][i];
        arr[j][i] = arr[i][j];
        arr[i][j] = temp;
      }
    }
  }
 
  // Function to rotate matrix
  // anticlockwise by 90 degree
  static void rotate(int[][] arr)
  {
    transpose(arr);
    reverseColumns(arr);
  }
 
  // Function to return the minimum number of flips
  static int solve(int[][] v, int n)
  {
    double Sum = 0.0;
 
    // Initialize Count vector
    int[][] c = new int[n][n];
    for (int i = 0; i < n; i++) {
      for (int j = 0; j < n; j++) {
        c[i][j] = 1;
      }
    }
 
    // Count 1 in each position for every rotation
    for (int t = 0; t < 4; t++) {
      rotate(v);
      for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
          if (v[i][j] == 1)
            c[i][j]++;
        }
      }
    }
 
    for (int i = 0; i < n; i++) {
      for (int j = 0; j < n; j++) {
        Sum += Math.min(c[i][j], 4 - c[i][j]);
      }
    }
 
    // Count Minimum reversal
    return (int)Math.round(Sum / 4);
  }
 
  // Driver Code
  public static void main (String[] args) {
 
    int[][] v
      = { { 1, 0, 0 }, { 0, 1, 0 }, { 1, 0, 1 } };
 
    int N = 3;
 
    // Function call
    System.out.println(solve(v, N));
  }
}
 
// This code is contributed by sanjoy_62.