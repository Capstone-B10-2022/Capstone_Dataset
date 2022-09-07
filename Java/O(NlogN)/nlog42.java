//https://www.geeksforgeeks.org/count-pairs-difference-equal-k/
import java.io.*;

class GFG {
	static int BS(int[] arr, int X, int low) {
		int high = arr.length - 1;
		int ans = arr.length;
		while(low <= high) {
			int mid = low + (high - low) / 2;
			if(arr[mid] >= X) {
				ans = mid;
				high = mid - 1;
			}
			else low = mid + 1;
		}
		return ans;
	}
	static int countPairsWithDiffK(int[] arr, int N, int k) {
		int count = 0;
		Arrays.sort(arr);
		for(int i = 0 ; i < N ; ++i) {
			int X = BS(arr, arr[i] + k, i + 1);
			if(X != N) {
				int Y = BS(arr, arr[i] + k + 1, i + 1);
				count += Y - X;
			}
		}

		return count;
	}
	public static void main (String[] args) {
		int arr[] = {1, 3, 5, 8, 6, 4, 6};
		int n = arr.length;
		int k = 2;
		System.out.println("Count of pairs with given diff is " +
							countPairsWithDiffK(arr, n, k));
		}
}
