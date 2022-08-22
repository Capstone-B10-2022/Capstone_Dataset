// Source: https://www.geeksforgeeks.org/rearrange-array-such-that-even-positioned-are-greater-than-odd/

// Java program to rearrange the elements
// in the array such that even positioned are
// greater than odd positioned elements
class GFG
{
  public static void rearrange(int[] arr, int n)
  {
    for(int i = 1; i < n; i++)
    {
 
      // if index is even
      if(i % 2 == 0)
      {
        if(arr[i] > arr[i - 1])
        {
 
          // swap two elements
          int temp = arr[i];
          arr[i] = arr[i - 1];
          arr[i - 1] = temp;
        }
      }
 
      // if index is odd
      else
      {
        if (arr[i] < arr[i - 1])
        {
 
          // swap two elements
          int temp = arr[i];
          arr[i] = arr[i - 1];
          arr[i - 1] = temp;
        }
      }
    }
 
    for (int i = 0; i < n; i++)
    {
      System.out.print(arr[i] + " ");
    }
  }
 
  // Driver code
  public static void main(String []args)
  {
    int n = 5;
    int arr[] = {1, 3, 2, 2, 5};
    rearrange(arr, n);
  }
}
