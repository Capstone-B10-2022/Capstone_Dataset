
// Java program for the above approach
import java.util.*;
 
public class nlog12
{
 
  // Function to find the rotation index k
  // that corresponds to the highest score
  static int bestIndex(int[] nums)
  {
    int N = nums.length;
    int gain = 0;
    int idx = 0;
    PriorityQueue<Integer> q
      = new PriorityQueue<Integer>();
 
    for (int i = 0; i < N; i++) {
      int diff = i - nums[i];
      if (diff >= 0) {
        gain++;
        q.add(diff);
      }
    }
 
    int current = gain;
    idx = 0;
 
    for (int i = 1; i <= N - 1; i++) {
      while (q.isEmpty() == false && (i > q.peek())) {
        q.remove();
        current--;
      }
      if (nums[i - 1] <= (N - 1)) {
        current++;
        q.add(i + (N - 1) - nums[i - 1]);
      }
      if (current > gain) {
        idx = i;
        gain = current;
      }
    }
    return idx;
  }
 
  // Driver Code
  public static void main(String args[])
  {
    int[] arr = { 2, 3, 1, 4, 0 };
    System.out.print(bestIndex(arr));
  }
}
 
// This code is contributed by Samim Hossain Mondal.