# Source: https://www.geeksforgeeks.org/delete-a-linked-list-node-at-a-given-position/

# Python program to delete a node in a linked list
# at a given position

# Node class


class Node:

	# Constructor to initialize the node object
	def __init__(self, data):
		self.data = data
		self.next = None


class LinkedList:

	# Constructor to initialize head
	def __init__(self):
		self.head = None

	# Function to insert a new node at the beginning
	def push(self, new_data):
		new_node = Node(new_data)
		new_node.next = self.head
		self.head = new_node

	# Given a reference to the head of a list
	# and a position, delete the node at a given position
	# This delete function code is contributed by Arabin Islam
	def deleteNodeAtGivenPosition(self, position):
		if self.head is None:
			return
		index = 0
		current = self.head
		while current.next and index < position:
			previous = current
			current = current.next
			index += 1

		if index == 0:
			self.head = self.head.next

		else:
			previous.next = current.next
			# current = None #Optional statement

	# Utility function to print the LinkedList

	def printList(self):
		temp = self.head
		while(temp):
			print(" %d " % (temp.data), end=" ")
			temp = temp.next


# Driver program to test above function
llist = LinkedList()
llist.push(7)
llist.push(1)
llist.push(3)
llist.push(2)
llist.push(8)

print("Created Linked List: ")
llist.printList()
llist.deleteNode(4)
print("\nLinked List after Deletion at position 4: ")
llist.printList()

# This code is contributed by Nikhil Kumar Singh(nickzuck_007)
