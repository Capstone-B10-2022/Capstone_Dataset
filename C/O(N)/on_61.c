// Source: https://www.geeksforgeeks.org/delete-a-linked-list-node-at-a-given-position/

// Simple C code to delete node at particular position

#include <stdio.h>
#include <stdlib.h>

void insert(int);
void display_List();
void delete (int);

struct node // Structure declaration
{
	int data;
	struct node* next; // Self referral pointer
}* head = NULL,
*tail
= NULL; // Initial value of Head and Tail pointer is NULL

void delete (int pos)
{
	struct node* temp = head; // Creating a temporary
							// variable pointing to head
	int i;
	if (pos == 0) {
		printf("\nElement deleted is : %d\n", temp->data);
		head = head->next; // Advancing the head pointer
		temp->next = NULL;
		free(temp); // Node is deleted
	}
	else {
		for (i = 0; i < pos - 1; i++) {
			temp = temp->next;
		}
		// Now temp pointer points to the previous node of
		// the node to be deleted
		struct node* del
			= temp->next; // del pointer points to the node
						// to be deleted
		temp->next = temp->next->next;
		printf("\nElement deleted is : %d\n", del->data);
		del->next = NULL;
		free(del); // Node is deleted
	}
	printf("\nUpdated Linked List is : \n");
	display_List();
	return;
}

void insert(int value)
{
	struct node* newnode; // Creating a new node
	newnode = (struct node*)malloc(
		sizeof(struct node)); // Allocating dynamic memory

	newnode->data = value; // Assigning value to newnode
	newnode->next = NULL;

	if (head == NULL) // Checking if List is empty
	{
		head = newnode;
		tail = newnode;
	}
	else // If not empty then...
	{
		tail->next = newnode;
		tail = newnode; // Updating the tail node with each
						// insertion
	}
	return;
}

void display_List()
{
	struct node* temp; // Creating a temporary pointer to
					// the structure
	temp = head; // temp points to head;
	while (temp != NULL) {
		if (temp->next == NULL) {
			printf(" %d->NULL", temp->data);
		}
		else {
			printf(" %d->", temp->data);
		}
		temp = temp->next; // Traversing the List till end
	}
	printf("\n");
	return;
}
// --Driver Code--
int main()
{
	insert(10);
	insert(20);
	insert(30);
	insert(40);
	insert(50);
	insert(60);
	printf("\n--Created Linked List--\n");
	display_List();
	printf("\nLinked List after deletion at position 0");
	delete (0); // List indexing starts from 0
	printf("\nLinked List after deletion at position 2");
	delete (2);
	return 0;
}
// This code is contributed by Sanjeeban Mukhopadhyay.
