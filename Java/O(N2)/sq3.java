// Java program for the above approach
class sq3 {
 
  // Function to rotate the array
  static void rotate(int[] arr, int N) {
    int temp = arr[0], i;
    for (i = 0; i < N - 1; i++)
      arr[i] = arr[i + 1];
    arr[N - 1] = temp;
    return;
  }
 
  // Function to calculate the
  // total score of a rotation
  static int calculate(int[] arr) {
    int score = 0;
    for (int i = 0; i < arr.length; i++) {
      if (arr[i] <= i) {
        score++;
      }
    }
    return score;
  }
 
  // Function to find the rotation index k
  // that corresponds to the highest score
  static int bestIndex(int[] nums) {
    int N = nums.length;
    int high_score = -1;
    int min_idx = 0;
 
    for (int i = 0; i < N; i++) {
      if (i != 0)
 
        // Rotates the array to left
        // by one position.
        rotate(nums, N);
 
      // Stores score of current rotation
      int cur_score = calculate(nums);
 
      if (cur_score > high_score) {
        min_idx = i;
        high_score = cur_score;
      }
    }
    return min_idx;
  }
 
  // Driver code
  public static void main(String args[]) {
    int[] arr = { 2, 3, 1, 4, 0 };
    System.out.println(bestIndex(arr));
  }
}
 
// This code is contributed by Saurabh Jaiswal