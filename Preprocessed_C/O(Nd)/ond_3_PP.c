# 1 "C:\\Users\\nikhi\\OneDrive\\Documents\\gitUploads\\Capstone_Dataset\\C\\O(Nd)\\ond_3.c"
# 1 "<built-in>"
# 1 "<command-line>"
# 1 "C:\\Users\\nikhi\\OneDrive\\Documents\\gitUploads\\Capstone_Dataset\\C\\O(Nd)\\ond_3.c"




void insertionSort(int A[], int size)
{
int i, key, j;
for (i = 1; i < size; i++)
{
 key = A[i];
 j = i-1;





 while (j >= 0 && A[j] > key)
 {
  A[j+1] = A[j];
  j = j-1;
 }
 A[j+1] = key;
}
}
