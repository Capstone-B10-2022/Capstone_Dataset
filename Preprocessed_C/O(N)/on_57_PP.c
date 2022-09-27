# 1 "C:\\Users\\nikhi\\OneDrive\\Documents\\gitUploads\\Capstone_Dataset\\C\\O(N)\\on_57.c"
# 1 "<built-in>"
# 1 "<command-line>"
# 1 "C:\\Users\\nikhi\\OneDrive\\Documents\\gitUploads\\Capstone_Dataset\\C\\O(N)\\on_57.c"





struct Node
{
int data;
struct Node *next;
};


void insertAfter(struct Node* prev_node, int new_data)
{

 if (prev_node == NULL) {
  printf("the given previous node cannot be NULL");
  return;
 }


 struct Node* new_node
  = (struct Node*)malloc(sizeof(struct Node));


 new_node->data = new_data;


 new_node->next = prev_node->next;


 prev_node->next = new_node;
}
