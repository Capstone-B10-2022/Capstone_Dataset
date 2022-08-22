// Java implementation of the approach
class ON_40 {

    /* Link list node */
    static class Node {
        int data;
        Node next;
    }

    /* A utility function to push a node */
    static Node push(Node head_ref, int new_data) {
        /* allocate node */
        Node new_node = new Node();

        /* put in the data */
        new_node.data = new_data;

        /* link the old list off the new node */
        new_node.next = (head_ref);

        /* move the head to point to the new node */
        (head_ref) = new_node;
        return head_ref;
    }

    /* A utility function to print linked list */
    static void printList(Node node) {
        while (node != null) {
            System.out.print(node.data + " -> ");
            node = node.next;
        }
        System.out.print("null");
    }

    // Function that rotates the given linked list
    // clockwise by k and returns the updated
    // head pointer
    static Node rightRotate(Node head, int k) {

        // If the linked list is empty
        if (head == null)
            return head;

        // len is used to store length of the linked list
        // tmp will point to the last node after this loop
        Node tmp = head;
        int len = 1;
        while (tmp.next != null) {
            tmp = tmp.next;
            len++;
        }

        // If k is greater than the size
        // of the linked list
        if (k > len)
            k = k % len;

        // Subtract from length to convert
        // it into left rotation
        k = len - k;

        // If no rotation needed then
        // return the head node
        if (k == 0 || k == len)
            return head;

        // current will either point to
        // kth or null after this loop
        Node current = head;
        int cnt = 1;
        while (cnt < k && current != null) {
            current = current.next;
            cnt++;
        }

        // If current is null then k is equal to the
        // count of nodes in the list
        // Don't change the list in this case
        if (current == null)
            return head;

        // current points to the kth node
        Node kthnode = current;

        // Change next of last node to previous head
        tmp.next = head;

        // Change head to (k+1)th node
        head = kthnode.next;

        // Change next of kth node to null
        kthnode.next = null;

        // Return the updated head pointer
        return head;
    }

    // Driver code
    public static void main(String args[]) {

        /*
         * The constructed linked list is:
         * 1.2.3.4.5
         */
        Node head = null;
        head = push(head, 5);
        head = push(head, 4);
        head = push(head, 3);
        head = push(head, 2);
        head = push(head, 1);

        int k = 2;

        // Rotate the linked list
        Node updated_head = rightRotate(head, k);

        // Print the rotated linked list
        printList(updated_head);
    }
}
