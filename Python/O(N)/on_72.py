# Source: https://www.geeksforgeeks.org/find-second-largest-element-array/

# Python3 program to find
# second largest element
# in an array
 
# Function to print
# second largest elements
def print2largest(arr, arr_size):
 
    # There should be atleast
    # two elements
    if (arr_size < 2):
        print(" Invalid Input ");
        return;
 
    largest = second = -2454635434;
 
    # Find the largest element
    for i in range(0, arr_size):
        largest = max(largest, arr[i]);
 
    # Find the second largest element
    for i in range(0, arr_size):
        if (arr[i] != largest):
            second = max(second, arr[i]);
 
    if (second == -2454635434):
        print("There is no second " +
              "largest element");
    else:
        print("The second largest " +
              "element is \n", second);
 
# Driver code
if __name__ == '__main__':
   
    arr = [12, 35, 1,
           10, 34, 1];
    n = len(arr);
    print2largest(arr, n);