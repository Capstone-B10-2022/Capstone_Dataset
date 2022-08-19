# Python3 implementation of the approach
 
''' Link list node '''
class Node:
 
    def __init__(self, data):
        self.data = data
        self.next = None
 
''' A utility function to push a node '''
def push(head_ref, new_data):
   
    ''' allocate node '''
    new_node = Node(new_data)
 
    ''' put in the data '''
    new_node.data = new_data
 
    ''' link the old list off the new node '''
    new_node.next = (head_ref)
 
    ''' move the head to point to the new node '''
    (head_ref) = new_node
 
    return head_ref
 
''' A utility function to print linked list '''
def printList(node):
    while (node != None):
        print(node.data, end=' -> ')
        node = node.next
    print("NULL")
 
# Function that rotates the given linked list
# clockwise by k and returns the updated
# head pointer
def rightRotate(head, k):
 
    # If the linked list is empty
    if (not head):
        return head
 
    # len is used to store length of the linked list
    # tmp will point to the last node after this loop
    tmp = head
    len = 1
 
    while (tmp.next != None):
        tmp = tmp.next
        len += 1
 
    # If k is greater than the size
    # of the linked list
    if (k > len):
        k = k % len
 
    # Subtract from length to convert
    # it into left rotation
    k = len - k
 
    # If no rotation needed then
    # return the head node
    if (k == 0 or k == len):
        return head
 
    # current will either point to
    # kth or None after this loop
    current = head
    cnt = 1
 
    while (cnt < k and current != None):
        current = current.next
        cnt += 1
 
    # If current is None then k is equal to the
    # count of nodes in the list
    # Don't change the list in this case
    if (current == None):
        return head
 
    # current points to the kth node
    kthnode = current
 
    # Change next of last node to previous head
    tmp.next = head
 
    # Change head to (k+1)th node
    head = kthnode.next
 
    # Change next of kth node to None
    kthnode.next = None
 
    # Return the updated head pointer
    return head
 
 
# Driver code
if __name__ == '__main__':
 
    ''' The constructed linked list is:
    1.2.3.4.5 '''
    head = None
    head = push(head, 5)
    head = push(head, 4)
    head = push(head, 3)
    head = push(head, 2)
    head = push(head, 1)
    k = 2
 
    # Rotate the linked list
    updated_head = rightRotate(head, k)
 
    # Print the rotated linked list
    printList(updated_head)