// Java program for the above approach.
import java.io.*;
class ON_30 {
 
  // Function to find the number of cyclic shifts
  static int find(int arr[], int N)
  {
    int maxele = Integer.MIN_VALUE;
    for(int i  = 0; i < N; i++){
      maxele = Math.max(arr[i], maxele);
    }
    int left = -1;
    int right = -1;
 
    // Placing left pointer
    // On its correct position
    for (int i = 0; i < N; i++) {
      if (arr[i] == maxele) {
        left = i;
        break;
      }
    }
 
    // Placing right pointer
    // On its correct position
    for (int i = N - 1; i >= 0; i--) {
      if (arr[i] == maxele) {
        right = i;
        break;
      }
    }
    int ans = (N / 2) - (right - left);
    if (ans <= 0) {
      return 0;
    }
    else {
      return ans;
    }
  }
 
  // Driver Code
  public static void main (String[] args) {
    int arr[] = { 3, 3, 5, 3, 3, 3 };
    int N = arr.length;
 
    // Function call
    System.out.print(find(arr, N));
  }
}