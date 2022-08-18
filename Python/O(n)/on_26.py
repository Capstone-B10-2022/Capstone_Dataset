# Python program to rotate a linked list
 
# Linked list Node
class Node :
 
    def __init__(self,d):
        self.data = d
        self.next = None
 
class LinkedList :
 
    def __init__(self):
        self.head = None
 
    # Function to left rotate a list
    # by x nodes in groups of y
    def leftRotate(self,x,y):
        prev = self.reverse(self.head, x, y - x, True)
        return self.reverse(prev, y, y, True)
 
    # Function to reverse list in
    # alternate groups of size m and n
    def reverse(self,head,m,n,isfirstHalf):
     
        if (head == None):
            return None
 
        current = head
        next = None
        prev = None
 
        count,k = 0,m
        if (isfirstHalf == False):
            k = n
 
        # Reverse first k nodes of linked list
        while (count < k and current != None) :
            next = current.next
            current.next = prev
            prev = current
            current = next
            count += 1
         
        # Next is now a pointer
        # to (k+1)th node
        # Recursively call for the list
        # starting from current and
        # make rest of the list
        # as next of first node
        if (next != None):
            head.next = self.reverse(next, m, n,~isfirstHalf)
 
        # prev is now head of input list
        return prev
 
    # Function to push a new node
    # on the front of the list.
    def push(self,new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node
 
    # Function to print list
    def printList(self):
        temp = self.head
        while (temp != None) :
            print(temp.data,end = " ")
            temp = temp.next
 
        print()
 
# Driver code
llist = LinkedList()
 
# Create a list
# 10->20->30->40->50->60
# ->70->80->90->100
for i in range(100,9,-10):
    llist.push(i)
 
print("Given list")
llist.printList()
 
llist.head = llist.leftRotate(2, 4)
 
print("Rotated Linked List")
llist.printList()