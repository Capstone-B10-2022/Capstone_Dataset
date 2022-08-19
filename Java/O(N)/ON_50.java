// Source: https://www.geeksforgeeks.org/move-zeroes-end-array/

// Java program to shift all zeros
// to right most side of array
// whthout affecting order of non-zero
// elements.
import java.util.*;
class ON_50
{
 
  // function to shift zeros 
  static void move_zeros_to_right(ArrayList<Integer> m)
  {
    int count = 0;
    for (int i = 0; i < m.size(); i++) {
      if (m.get(i) == 0) {
        count++;
 
        // deleting the element from vector
        m.remove(i);
        i--;
      }
    }
 
    for (int i = 0; i < count; i++)
    {
 
      // inserting the zero into arraylist
      m.add(0);
    }
    System.out.println("array after shifting zeros to right side: ");
    for (int i = 0; i < m.size(); i++)
    {
 
      // printing desired arraylist
      System.out.print(m.get(i) + " ");
    }
  }
 
  // Driver Code
  public static void main(String[] args)
  {
    ArrayList<Integer> m = new ArrayList<>(Arrays.asList(5, 6, 0, 4, 6, 0, 9, 0, 8));
 
    // function call
    move_zeros_to_right(m);
  }
}
