// Source: https://www.geeksforgeeks.org/rearrange-positive-and-negative-numbers/

// Java program for
// moving negative numbers to left
// while maintaining the order
class ON_56 {
 
    static int[] rotateSubArray(int[] arr, int l, int r) {
      int temp = arr[r];
      for (int j = r; j > l - 1; j--) {
        arr[j] = arr[j - 1];
      }
      arr[l] = temp;
   
      return arr;
    }
   
    static int[] moveNegative(int[] arr) {
   
      int last_negative_index = -1;
   
      for (int i = 0; i < arr.length; i++) {
        if (arr[i] < 0) {
          last_negative_index += 1;
          int temp = arr[i];
          arr[i] = arr[last_negative_index];
          arr[last_negative_index] = temp;
   
          // Done to manage order too
          if (i - last_negative_index >= 2)
            rotateSubArray(arr, last_negative_index + 1, i);
        }
      }
   
      return arr;
    }
   
    // Driver Code
    public static void main(String args[]) {
      int[] arr = { 5, 5, -3, 4, -8, 0, -7, 3, -9, -3, 9, -2, 1 };
      arr = moveNegative(arr);
   
      for (int i : arr) {
        System.out.print(i + " ");
      }
    }
  }
