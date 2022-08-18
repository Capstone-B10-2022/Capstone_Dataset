/*package whatever //do not write package name here */
 
import java.io.*;
 
class ON_28 {
  // Function to find maximum possible product
  static int findMax(String S)
  {
    int N = S.length();
    int f = (int)S.charAt(0) - (int)'0';
    int l = (int)S.charAt(N - 1) - (int)'0';
 
    int Max = f * l;
 
    for (int i = 1; i < N; i++) {
      f = (int)S.charAt(i) - (int)'0';
      l = (int)S.charAt(i-1) - (int)'0';
      Max = Math.max(Max, f * l);
    }
 
    // Return the maximum product as the answer
    return Max;
  }
 
  /* Driver program to test above function*/
  public static void main(String args[])
  {
    String Str = "12345";
 
    // Function Call
    System.out.print(findMax(Str));
  }
}