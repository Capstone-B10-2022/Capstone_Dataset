// Java program for the above approach
import java.io.*;
import java.lang.*;
import java.util.*;
 
class OND_3 {
 
  // Function to find the minimum number
  // of steps
  static void findMinimumNumberOfSteps(int arr[],
                                       int K)
  {
 
    // Variable to store the answer
    int time = 0;
 
    // Traverse in the while loop
    while (arr[K] != 0) {
 
      // Iterate over the loop
      for (int i = 0; i < arr.length; i++) {
 
        // Check the condition and
        // decrease the value
        if (arr[i] > 0) {
          arr[i] -= 1;
          time++;
        }
 
        // Break the loop
        if (arr[K] == 0)
          break;
      }
    }
 
    // Print the result
    System.out.println(time);
  }
 
  // Driver Code
  public static void main (String[] args) {
    int arr[] = { 2, 3, 2 };
    int K = 2;
    findMinimumNumberOfSteps(arr, K);
  }
}