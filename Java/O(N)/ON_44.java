// Source: https://www.geeksforgeeks.org/rearrange-array-arri/

// Java program for rearrange an
// array such that arr[i] = i.
import java.util.Arrays;
 
class ON_44
{
    public static void main(String[] args)
    {
        int[] arr = { -1, -1, 6, 1, 9, 3, 2, -1, 4, -1 };
        for (int i = 0; i < arr.length;)
        {
            if (arr[i] >= 0 && arr[i] != i)
            {
                int ele = arr[arr[i]];
                arr[arr[i]] = arr[i];
                arr[i] = ele;
            }
            else
            {
                i++;
            }
        }
        System.out.println(Arrays.toString(arr));
    }
}
