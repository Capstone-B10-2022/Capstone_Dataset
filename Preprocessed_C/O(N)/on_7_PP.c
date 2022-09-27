# 1 "C:\\Users\\nikhi\\OneDrive\\Documents\\gitUploads\\Capstone_Dataset\\C\\O(N)\\on_7.c"
# 1 "<built-in>"
# 1 "<command-line>"
# 1 "C:\\Users\\nikhi\\OneDrive\\Documents\\gitUploads\\Capstone_Dataset\\C\\O(N)\\on_7.c"


void leftRotate(int arr[], int d, int n)
{
  int i, j;
  if(d == 0 || d == n)
    return;

  if(d > n)
    d = d % n;
  i = d;
  j = n - d;
  while (i != j)
  {
    if(i < j)
    {
      swap(arr, d-i, d+j-i, i);
      j -= i;
    }
    else
    {
      swap(arr, d-i, d, j);
      i -= j;
    }

  }

  swap(arr, d-i, d, i);
}
