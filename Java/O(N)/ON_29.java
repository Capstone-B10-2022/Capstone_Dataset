// Java program to rotate a linked list
 
class ON_29 {
    Node head;
 
    // Linked list Node
    public class Node {
        int data;
        Node next;
        Node(int d)
        {
            data = d;
            next = null;
        }
    }
 
    // Function to left rotate a list
    // by x nodes in groups of y
    Node leftRotate(int x, int y)
    {
        Node prev = reverse(head, x,
                            y - x, true);
        return reverse(prev, y, y, true);
    }
 
    // Function to reverse list in
    // alternate groups of size m and n
    Node reverse(Node head, int m, int n,
                boolean isfirstHalf)
    {
        if (head == null)
            return null;
 
        Node current = head;
        Node next = null;
        Node prev = null;
 
        int count = 0, k = m;
        if (!isfirstHalf)
            k = n;
 
        // Reverse first k nodes of linked list
        while (count < k && current != null) {
            next = current.next;
            current.next = prev;
            prev = current;
            current = next;
            count++;
        }
 
        // Next is now a pointer
        // to (k+1)th node
        // Recursively call for the list
        // starting from current and
        // make rest of the list
        // as next of first node
        if (next != null)
            head.next
                = reverse(next, m, n,
                        !isfirstHalf);
 
        // prev is now head of input list
        return prev;
    }
 
    // Function to push a new node
    // on the front of the list.
    void push(int new_data)
    {
        Node new_node = new Node(new_data);
        new_node.next = head;
        head = new_node;
    }
 
    // Function to print list
    void printList()
    {
        Node temp = head;
        while (temp != null) {
            System.out.print(temp.data + " ");
            temp = temp.next;
        }
        System.out.println();
    }
 
    // Driver code
    public static void main(String args[])
    {
        ON_29 llist = new ON_29();
 
        // Create a list
        // 10->20->30->40->50->60
        // ->70->80->90->100
        for (int i = 100; i >= 10; i -= 10)
            llist.push(i);
 
        System.out.println("Given list");
        llist.printList();
 
        llist.head = llist.leftRotate(2, 4);
 
        System.out.println("Rotated Linked List");
        llist.printList();
    }
}