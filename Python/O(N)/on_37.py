# Python code to implement above approach
 
# Function to print array
def print1(arr, N):
    for i in range(N):
        print(arr[i], end = " ");
 
# Function to reverse the array
# from start to end index
def reverse(arr, start, end):
    temp = 0;
    size = end - start;
 
    # Reversal based on pointer approach
    for i in range(size//2):
        temp = arr[i + start];
        arr[i + start] = arr[start + size - i - 1];
        arr[start + size - i - 1] = temp;
 
    return arr;
 
# Function to right rotate the array K times
def right(arr, K, N):
    arr = reverse(arr, 0, N - K);
    arr = reverse(arr, N - K, N);
    arr = reverse(arr, 0, N);
    print1(arr, N);
 
# Driver code
if __name__ == '__main__':
    arr = [1, 2, 3, 4, 5, 6];
    N = len(arr);
    K = 2;
    right(arr, K, N);