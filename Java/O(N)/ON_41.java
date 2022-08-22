// java program for the above approach
import java.io.*;
import java.lang.*;
import java.util.*;
 
class ON_41 {
 
  // Utility function to rotate the digits of
  // array elements such that array elements are
  // in placed even-odd or odd-even alternately
  static boolean is_possible(int arr[], int check)
  {
 
    // Checks if array can be converted
    // into even-odd or odd-even form
    boolean exists = true;
 
    // Store array elements
    int cpy[] = arr.clone();
    boolean flag;
    // Traverse the array
    for (int i = 0; i < arr.length; i++) {
 
      // Check if arr[i] is already
      // at correct position
      if (arr[i] % 2 == check) {
        // Changes the
        // parity of check
        check = (check == 0 ? 1 : 0);
        continue;
      }
 
      // Checks if it is possible
      // to modify the number arr[i]
      // by rotating the digits of
      // the number anticlockwise
      flag = false;
 
      // Stores the number arr[i] as
      // string
      String strEle = Integer.toString(arr[i]);
 
      // Traverse over the digits of
      // the current element
      for (int j = 0; j < strEle.length(); j++) {
 
        // Checks if parity of check and
        // current digit is same or not
        if ((strEle.charAt(j) - '0') % 2 == check) {
 
          // Rotates the string by j + 1 times
          // in anticlockwise
          arr[i] = Integer.parseInt(
            strEle.substring(j + 1)
            + strEle.substring(0, j + 1));
 
          // Marks the flag
          // as true and break
          flag = true;
          break;
        }
      }
 
      // If flag is false
      if (flag == false) {
        // Update exists
        exists = false;
        break;
      }
 
      // Changes the
      // parity of check
      check = (check == 0 ? 1 : 0);
    }
 
    // Checks if arr[] cannot be
    // modified, then returns false
    if (!exists) {
      arr = cpy;
      return false;
    }
 
    // Otherwise, return true
    else
      return true;
  }
 
  // Function to rotate the digits of array
  // elements such that array elements are
  // in the form of even-odd or odd-even form
  static void convert_arr(int arr[])
  {
 
    // If array elements can be arranged
    // in even-odd manner alternately
    if (is_possible(arr, 0)) {
      for (int v : arr) {
        System.out.print(v + " ");
      }
    }
 
    // If array elements can be arranged
    // in odd-even manner alternately
    else if (is_possible(arr, 1)) {
      for (int v : arr) {
        System.out.print(v + " ");
      }
    }
 
    // Otherwise, prints -1
    else
      System.out.println(-1);
  }
 
  // Driver code
  public static void main(String[] args)
  {
    // Given array
    int arr[] = { 143, 251, 534, 232, 854 };
 
    // FUnction call
    convert_arr(arr);
  }
}
