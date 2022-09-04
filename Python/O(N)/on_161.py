# Source: https://www.geeksforgeeks.org/linked-list-set-2-inserting-a-node/

# This function is defined in Linked List class
# Appends a new node at the end. This method is
# defined inside LinkedList class shown above


def append(self, new_data):

		# 1. Create a new node
		# 2. Put in the data
		# 3. Set next as None
		new_node = Node(new_data)

		# 4. If the Linked List is empty, then make the
		# new node as head
		if self.head is None:
			self.head = new_node
			return

		# 5. Else traverse till the last node
		last = self.head
		while (last.next):
			last = last.next

		# 6. Change the next of last node
		last.next = new_node
