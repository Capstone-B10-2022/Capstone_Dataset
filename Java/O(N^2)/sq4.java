// Java program to print
// all possible rotations
// of the given array
class sq4{
     
// Global declaration of array
static int arr[] = new int[10000];
 
// Function to reverse array
// between indices s and e
public static void reverse(int arr[],
                           int s, int e)
{
    while(s < e)
    {
        int tem = arr[s];
        arr[s] = arr[e];
        arr[e] = tem;
        s = s + 1;
        e = e - 1;
    }
}
 
// Function to generate all
// possible rotations of array
public static void fun(int arr[], int k)
{
    int n = 4 - 1;
    int v = n - k;
     
    if (v >= 0)
    {
        reverse(arr, 0, v);
        reverse(arr, v + 1, n);
        reverse(arr, 0, n);
    }
}
 
// Driver code
public static void main(String args[])
{
    arr[0] = 1;
    arr[1] = 2;
    arr[2] = 3;
    arr[3] = 4;
     
    for(int i = 0; i < 4; i++)
    {
        fun(arr, i);
         
        System.out.print("[");
        for(int j = 0; j < 4; j++)
        {
            System.out.print(arr[j] + ", ");
        }
        System.out.print("]");
    }
}
}
 
// This code is contributed by gk74533