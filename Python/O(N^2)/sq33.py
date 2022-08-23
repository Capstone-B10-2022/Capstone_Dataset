# Python code for the above approach

#https://www.geeksforgeeks.org/minimize-number-of-rotations-on-array-a-such-that-it-becomes-equal-to-b/
# Function to check if two arrays are equal
def check(A, B, N):
	flag = True;
	for i in range(N):
		if (A[i] != B[i]):
			flag = False;
			break;
	return flag;

# Function to left rotate an array
def Leftrotate(A, N):
	temp = A[0];
	for i in range(N - 1):
		A[i] = A[i + 1];
	A[N - 1] = temp;

# Function to right rotate an array
def Rightrotate(A, N):
	temp = A[N - 1];
	for i in range(N - 1, 0, -1):
		A[i] = A[i - 1];
	A[0] = temp;

# Function to minimize number of rotations
def minRotations(A, B, N):
	C = [0] * N
	for i in range(N):
		C[i] = A[i];
	a = 0
	b = 0

	# Right rotate the array
	# till it is equal to B
	while (check(A, B, N) == False):
		Rightrotate(A, N);
		a += 1

	# Left rotate the array
	# till it is equal to B
	while (check(C, B, N) == False):
		Leftrotate(C, N);
		b += 1

	ans = min(a, b);
	return ans;

# Driver code
A = [13, 12, 7, 18, 4, 5, 1];
B = [12, 7, 18, 4, 5, 1, 13];
N = len(A)

ans = minRotations(A, B, N);
print(ans);

# This code is contributed by gfgking
