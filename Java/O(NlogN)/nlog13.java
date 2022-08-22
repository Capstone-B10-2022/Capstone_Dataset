// Java program to implement
// the above approach
class nlog13{

// Structure of an AVL Tree Node
static class Node
{
	int key;
	Node left;
	Node right;
	int height;
	
	// Size of the tree rooted
	// with this Node
	int size;

	public Node(int key)
	{
		this.key = key;
		this.left = this.right = null;
		this.size = this.height = 1;
	}
};

// Helper class to pass Integer
// as reference
static class RefInteger
{
	Integer value;
	
	public RefInteger(Integer value)
	{
		this.value = value;
	}
}

// Utility function to get height
// of the tree rooted with N
static int height(Node N)
{
	if (N == null)
		return 0;
		
	return N.height;
}

// Utility function to find size of
// the tree rooted with N
static int size(Node N)
{
	if (N == null)
		return 0;
		
	return N.size;
}

// Utility function to get maximum
// of two integers
static int max(int a, int b)
{
	return (a > b) ? a : b;
}

// Utility function to right rotate
// subtree rooted with y
static Node rightRotate(Node y)
{
	Node x = y.left;
	Node T2 = x.right;

	// Perform rotation
	x.right = y;
	y.left = T2;

	// Update heights
	y.height = max(height(y.left),
				height(y.right)) + 1;
	x.height = max(height(x.left),
				height(x.right)) + 1;

	// Update sizes
	y.size = size(y.left) +
			size(y.right) + 1;
	x.size = size(x.left) +
			size(x.right) + 1;

	// Return new root
	return x;
}

// Utility function to left rotate
// subtree rooted with x
static Node leftRotate(Node x)
{
	Node y = x.right;
	Node T2 = y.left;

	// Perform rotation
	y.left = x;
	x.right = T2;

	// Update heights
	x.height = max(height(x.left),
				height(x.right)) + 1;
	y.height = max(height(y.left),
				height(y.right)) + 1;

	// Update sizes
	x.size = size(x.left) +
			size(x.right) + 1;
	y.size = size(y.left) +
			size(y.right) + 1;

	// Return new root
	return y;
}

// Function to obtain Balance factor
// of Node N
static int getBalance(Node N)
{
	if (N == null)
		return 0;

	return height(N.left) -
		height(N.right);
}

// Function to insert a new key to the
// tree rooted with Node
static Node insert(Node Node, int key,
				RefInteger count)
{
	
	// Perform the normal BST rotation
	if (Node == null)
		return (new Node(key));

	if (key < Node.key)
		Node.left = insert(Node.left,
						key, count);
	else
	{
		Node.right = insert(Node.right,
							key, count);

		// Update count of smaller elements
		count.value = count.value +
				size(Node.left) + 1;
	}

	// Update height and size of the ancestor
	Node.height = max(height(Node.left),
					height(Node.right)) + 1;
	Node.size = size(Node.left) +
				size(Node.right) + 1;

	// Get the balance factor of the ancestor
	int balance = getBalance(Node);

	// Left Left Case
	if (balance > 1 && key < Node.left.key)
		return rightRotate(Node);

	// Right Right Case
	if (balance < -1 && key > Node.right.key)
		return leftRotate(Node);

	// Left Right Case
	if (balance > 1 && key > Node.left.key)
	{
		Node.left = leftRotate(Node.left);
		return rightRotate(Node);
	}

	// Right Left Case
	if (balance < -1 && key < Node.right.key)
	{
		Node.right = rightRotate(Node.right);
		return leftRotate(Node);
	}
	return Node;
}

// Function to generate an array which
// contains count of smaller elements
// on the right
static void constructLowerArray(int arr[],
	RefInteger[] countSmaller, int n)
{
	int i, j;
	Node root = null;

	for(i = 0; i < n; i++)
		countSmaller[i] = new RefInteger(0);

	// Insert all elements in the AVL Tree
	// and get the count of smaller elements
	for(i = n - 1; i >= 0; i--)
	{
		root = insert(root, arr[i],
				countSmaller[i]);
	}
}

// Function to find the number
// of elements which are greater
// than all elements on its left
// and K elements on its right
static int countElements(int A[], int n,
						int K)
{
	int count = 0;

	// Stores the count of smaller
	// elements on its right
	RefInteger[] countSmaller = new RefInteger[n];
	constructLowerArray(A, countSmaller, n);

	int maxi = Integer.MIN_VALUE;
	for(int i = 0; i <= (n - K - 1); i++)
	{
		if (A[i] > maxi &&
			countSmaller[i].value >= K)
		{
			count++;
			maxi = A[i];
		}
	}
	return count;
}

// Driver Code
public static void main(String[] args)
{
	int A[] = { 2, 5, 1, 7, 3, 4, 0 };
	int n = A.length;
	int K = 3;

	System.out.println(countElements(A, n, K));
}
}

// This code is contributed by sanjeev2552
