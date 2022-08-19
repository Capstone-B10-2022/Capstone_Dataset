// Java program for above approach
import java.util.*;
 
class ON_35{
 
  // Function to find no of iterations.
  static int minZero(Vector<Integer> A, int n)
  {
 
    // Initialize count c = 0.
    int c = 0;
 
    // if zero is already present
    // in array return c.
    if (Collections.min(A) == 0)
      return c;
 
    // Iterate till minimum
    // in array becomes zero.
    while (Collections.min(A) != 0) {
 
      // Copy array element to A1
      Vector<Integer> A1 = (Vector<Integer>) A.clone();
 
      // Pop first element and
      // append it to last
      int x = A.get(0);
      A.remove(0);
      A.add(x);
 
      // Perform subtraction
      for (int i = 0; i < n; i++)
        A.set(i, Math.abs(A.get(i) - A1.get(i)));
 
      // Increment count by 1
      c += 1;
    }
 
    // Return value of count c
    return c;
  }
 
  // Driver Code
  public static void main(String[] args)
  {
 
    // Original array
    Integer []arr = { 2, 6, 3, 4, 8, 7 };
    Vector<Integer> v = new Vector<Integer>();
    Collections.addAll(v, arr);
     
    // Calling method minZero
    int x = minZero(v, arr.length);
 
    // Print the result
    System.out.print(x);
 
  }
}