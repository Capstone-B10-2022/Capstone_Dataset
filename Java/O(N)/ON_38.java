// Java code to implement above approach
import java.util.*;
 
class ON_38{
 
// Function to print the array
static void print(int arr[], int N)
{
    for (int i = 0; i < N; i++)
        System.out.print(arr[i]+ " ");
}
 
// Function to reverse the array
// from start to end index
static int[] reverse(int arr[], int start, int end)
{
    int temp;
    int size = end - start;
 
    // Reversal based on pointer approach
    for (int i = 0; i < (size / 2); i++) {
        temp = arr[ i + start];
        arr[i + start] = arr[start
                             + size - i - 1];
        arr[start + size - i - 1] = temp;
    }
    return arr;
}
 
// Function to right rotate the array K times
static void right(int arr[], int K, int N)
{
    arr = reverse(arr, 0, N - K);
    arr = reverse(arr, N - K, N);
    arr = reverse(arr, 0, N);
    print(arr, N);
}
 
// Driver code
public static void main(String[] args)
{
    int arr[] = { 1, 2, 3, 4, 5, 6 };
    int N = arr.length;
    int K = 2;
    right(arr, K, N);
}
}