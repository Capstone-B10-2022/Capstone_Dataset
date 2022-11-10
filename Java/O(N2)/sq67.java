/*Construct a BST from given pre-order traversal
for example if the given traversal is {10, 5, 1, 7, 40, 50},
then the output should be the root of the following tree.
	10
/ \
5	 40
/ \	 \
1 7	 50 */

class Node {
	int data;
	Node left, right;
	Node(int data)
	{
		this.data = data;
		this.left = this.right = null;
	}
}

class sq67 {
	private static Node node;

	// This will create the BST
	public static Node createNode(Node node, int data)
	{
		if (node == null)
			node = new Node(data);

		if (node.data > data)
			node.left = createNode(node.left, data);
		if (node.data < data)
			node.right = createNode(node.right, data);

		return node;
	}

	// A wrapper function of createNode
	public static void create(int data)
	{
		node = createNode(node, data);
	}
	// A function to print BST in inorder
	public static void inorderRec(Node root)
	{
		if (root != null) {
			inorderRec(root.left);
			System.out.println(root.data);
			inorderRec(root.right);
		}
	}

	// Driver Code
	public static void main(String[] args)
	{
		int[] nodeData = { 10, 5, 1, 7, 40, 50 };

		for (int i = 0; i < nodeData.length; i++) {
			create(nodeData[i]);
		}
		inorderRec(node);
	}
}
