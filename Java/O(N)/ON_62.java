// Source: https://www.geeksforgeeks.org/move-negative-numbers-beginning-positive-end-constant-extra-space/

// Java program to move all negative numbers to the
// beginning and all positive numbers to the end with
// constant extra space
 
public class ON_62 {
 
    // a utility function to swap two elements of an array
    public static void swap(int[] ar, int i, int j)
    {
        int t = ar[i];
        ar[i] = ar[j];
        ar[j] = t;
    }
 
    // function to shilf all negative integers to the left
    // and all positive integers to the right
    // using Dutch National Flag Algorithm
    public static void move(int[] ar)
    {
        int low = 0;
        int high = ar.length - 1;
        while (low <= high) {
            if (ar[low] <= 0)
                low++;
            else
                swap(ar, low, high--);
        }
    }
 
    // Driver code
    public static void main(String[] args)
    {
        int[] ar = { 1, 2,  -4, -5, 2, -7, 3,
                     2, -6, -8, -9, 3, 2,  1 };
        move(ar);
        for (int e : ar)
            System.out.print(e + " ");
    }
}
