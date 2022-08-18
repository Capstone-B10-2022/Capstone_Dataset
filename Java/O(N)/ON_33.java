// Java Program to implement 
// the above approach 
  
public class ON_33 { 
  
    // Function to return the 
    // count of rotations 
    public static int countRotation(int[] arr, 
                                    int low, 
                                    int high) 
    { 
        // If array is not rotated 
        if (low > high) { 
            return 0; 
        } 
  
        int mid = low + (high - low) / 2; 
  
        // Check if current element is 
        // greater than the next 
        // element 
  
        if (mid < high 
            && arr[mid] > arr[mid + 1]) { 
            // the next element is 
            // the smallest 
            return mid + 1; 
        } 
  
        // Check if current element is 
        // smaller than it's previous 
        // element 
        if (mid > low 
            && arr[mid] < arr[mid - 1]) { 
            // Current element is 
            // the smallest 
            return mid; 
        } 
  
        // Check if current element is 
        // greater than lower bound 
  
        if (arr[mid] > arr[low]) { 
            // The sequence is increasing 
            // so far 
            // Search for smallest 
            // element on the right 
            // subarray 
            return countRotation(arr, 
                                mid + 1, 
                                high); 
        } 
  
        if (arr[mid] < arr[high]) { 
            // Smallest element lies on the 
            // left subarray 
            return countRotation(arr, 
                                low, 
                                mid - 1); 
        } 
  
        else { 
            // Search for the smallest 
            // element on both subarrays 
            int rightIndex = countRotation(arr, 
                                        mid + 1, 
                                        high); 
            int leftIndex = countRotation(arr, 
                                        low, 
                                        mid - 1); 
  
            if (rightIndex == 0) { 
                return leftIndex; 
            } 
  
            return rightIndex; 
        } 
    } 
  
    // Driver Program 
    public static void main(String[] args) 
    { 
        int[] arr1 = { 4, 5, 1, 2, 3 }; 
  
        System.out.println( 
            countRotation( 
                arr1, 
                0, arr1.length 
                    - 1)); 
    } 
} 