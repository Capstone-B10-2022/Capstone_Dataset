# 1 "C:\\Users\\nikhi\\OneDrive\\Documents\\gitUploads\\Capstone_Dataset\\C\\O(N)\\on_58.c"
# 1 "<built-in>"
# 1 "<command-line>"
# 1 "C:\\Users\\nikhi\\OneDrive\\Documents\\gitUploads\\Capstone_Dataset\\C\\O(N)\\on_58.c"




void append(struct Node** head_ref, int new_data)
{

 struct Node* new_node = (struct Node*) malloc(sizeof(struct Node));

 struct Node *last = *head_ref;


 new_node->data = new_data;



 new_node->next = NULL;


 if (*head_ref == NULL)
 {
 *head_ref = new_node;
 return;
 }


 while (last->next != NULL)
  last = last->next;


 last->next = new_node;
 return;
}
