// Source: https://www.geeksforgeeks.org/find-the-minimum-distance-between-two-numbers/

class ON_97
{
	int minDist(int arr[], int n, int x, int y)
	{
		
	//previous index and min distance
	int i=0,p=-1, min_dist=Integer.MAX_VALUE;
	
	for(i=0 ; i<n ; i++)
	{
		if(arr[i] ==x || arr[i] == y)
		{
			//we will check if p is not equal to -1 and
			//If the element at current index matches with
			//the element at index p , If yes then update
			//the minimum distance if needed
			if(p != -1 && arr[i] != arr[p])
				min_dist = Math.min(min_dist,i-p);
			
			//update the previous index
			p=i;
		}
	}
	//If distance is equal to int max
	if(min_dist==Integer.MAX_VALUE)
	return -1;
	return min_dist;
}

	/* Driver program to test above functions */
	public static void main(String[] args) {
		ON_97 min = new ON_97();
		int arr[] = {3, 5, 4, 2, 6, 3, 0, 0, 5, 4, 8, 3};
		int n = arr.length;
		int x = 3;
		int y = 6;

		System.out.println("Minimum distance between " + x + " and " + y
				+ " is " + min.minDist(arr, n, x, y));
	}
}

