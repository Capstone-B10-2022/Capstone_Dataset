// Java Program to solve queries on Left and Right
// Circular shift on array
class ON_24 {
 
    // Function to solve query of type 1 x.
    static int querytype1(int toRotate, int times, int n)
    {
 
        // Decreasing the absolute rotation
        toRotate = (toRotate - times) % n;
        return toRotate;
    }
 
    // Function to solve query of type 2 y.
    static int querytype2(int toRotate, int times, int n)
    {
        // Increasing the absolute rotation.
        toRotate = (toRotate + times) % n;
        return toRotate;
    }
 
    // Function to solve queries of type 3 l r.
    static void querytype3(int toRotate, int l, int r,
                           int preSum[], int n)
    {
        // Finding absolute l and r.
        l = (l + toRotate + n) % n;
        r = (r + toRotate + n) % n;
 
        // if l is before r.
        if (l <= r)
            System.out.println(preSum[r + 1] - preSum[l]);
 
        // If r is before l.
        else
            System.out.println(preSum[n] + preSum[r + 1]
                               - preSum[l]);
    }
 
    // Wrapper Function solve all queries.
    static void wrapper(int a[], int n)
    {
        int preSum[] = new int[n + 1];
        preSum[0] = 0;
 
        // Finding Prefix sum
        for (int i = 1; i <= n; i++)
            preSum[i] = preSum[i - 1] + a[i - 1];
 
        int toRotate = 0;
 
        // Solving each query
        toRotate = querytype1(toRotate, 3, n);
        querytype3(toRotate, 0, 2, preSum, n);
        toRotate = querytype2(toRotate, 1, n);
        querytype3(toRotate, 1, 4, preSum, n);
    }
 
    // Driver Program
    public static void main(String args[])
    {
        int arr[] = { 1, 2, 3, 4, 5 };
        int N = arr.length;
        wrapper(arr, N);
    }
}
