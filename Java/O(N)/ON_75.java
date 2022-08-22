// Source: https://www.geeksforgeeks.org/find-second-largest-element-array/

// Java program to find second largest
// element in an array
class ON_75{
 
    // Function to print the second largest elements
    static void print2largest(int arr[], int arr_size)
    {
        int i, first, second;
     
        // There should be atleast two elements
        if (arr_size < 2)
        {
            System.out.printf(" Invalid Input ");
            return;
        }
     
        int largest = second = Integer.MIN_VALUE;
     
        // Find the largest element
        for(i = 0; i < arr_size; i++)
        {
            largest = Math.max(largest, arr[i]);
        }
     
        // Find the second largest element
        for(i = 0; i < arr_size; i++)
        {
            if (arr[i] != largest)
                second = Math.max(second, arr[i]);
        }
        if (second == Integer.MIN_VALUE)
            System.out.printf("There is no second " +
                              "largest element\n");
        else
            System.out.printf("The second largest " +
                              "element is %d\n", second);
    }
     
    // Driver code
    public static void main(String[] args)
    {
        int arr[] = { 12, 35, 1, 10, 34, 1 };
        int n = arr.length;
         
        print2largest(arr, n);
    }
    }
