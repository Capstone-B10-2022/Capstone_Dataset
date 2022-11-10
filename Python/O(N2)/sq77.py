# Construct a BST from given pre-order traversal
# for example if the given traversal is {10, 5, 1, 7, 40, 50},
# then the output should be the root of the following tree.
#	 10
# / \
# 5	 40
# / \	 \
# 1 7	 50
class Node:
	data = 0
	left = None
	right = None

	def __init__(self, data):
		self.data = data
		self.left = None
		self.right = None

class CreateBSTFromPreorder:
	node = None
	# This will create the BST
	@staticmethod
	def createNode(node, data):
		if (node == None):
			node = Node(data)
		if (node.data > data):
			node.left = CreateBSTFromPreorder.createNode(node.left, data)
		if (node.data < data):
			node.right = CreateBSTFromPreorder.createNode(node.right, data)
		return node
	
	# A wrapper function of createNode
	@staticmethod
	def create(data):
		CreateBSTFromPreorder.node = CreateBSTFromPreorder.createNode(
			CreateBSTFromPreorder.node, data)
		
	# A function to print BST in inorder
	@staticmethod
	def inorderRec(root):
		if (root != None):
			CreateBSTFromPreorder.inorderRec(root.left)
			print(root.data)
			CreateBSTFromPreorder.inorderRec(root.right)
			
	# Driver Code
	@staticmethod
	def main(args):
		nodeData = [10, 5, 1, 7, 40, 50]
		i = 0
		while (i < len(nodeData)):
			CreateBSTFromPreorder.create(nodeData[i])
			i += 1
		CreateBSTFromPreorder.inorderRec(CreateBSTFromPreorder.node)

if __name__ == "__main__":
	CreateBSTFromPreorder.main([])

# This code is contributed by mukulsomukesh
