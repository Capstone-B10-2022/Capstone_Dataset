# 1 "C:\\Users\\nikhi\\OneDrive\\Documents\\gitUploads\\Capstone_Dataset\\C\\O(N)\\on_49.c"
# 1 "<built-in>"
# 1 "<command-line>"
# 1 "C:\\Users\\nikhi\\OneDrive\\Documents\\gitUploads\\Capstone_Dataset\\C\\O(N)\\on_49.c"


void printRepeating(int arr[], int size)
{
int xor = arr[0];
int set_bit_no;
int i;
int n = size - 2;
int x = 0, y = 0;


for(i = 1; i < size; i++)
 xor ^= arr[i];
for(i = 1; i <= n; i++)
 xor ^= i;


set_bit_no = xor & ~(xor-1);



for(i = 0; i < size; i++)
{
 if(arr[i] & set_bit_no)
 x = x ^ arr[i];
 else
 y = y ^ arr[i];
}
for(i = 1; i <= n; i++)
{
 if(i & set_bit_no)
 x = x ^ i;
 else
 y = y ^ i;
}

printf("n The two repeating elements are %d & %d ", x, y);
}


int main()
{
int arr[] = {4, 2, 4, 5, 2, 3, 1};
int arr_size = sizeof(arr)/sizeof(arr[0]);
printRepeating(arr, arr_size);
getchar();
return 0;
}
