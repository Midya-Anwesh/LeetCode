/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* modifiedList(int* nums, int numsSize, struct ListNode* head) {
    // creating hash table
    int *table = (int *)calloc(sizeof(int), 100001);
    for (int i = 0; i < numsSize; table[nums[i++]]++);

    // defining pointers to travrese on ll
    struct ListNode *pre = NULL, *curr = head;

    while (curr != NULL){
        // if we have to delete a node
        if ( table[(curr -> val)] ){
            // if head is to be deleted
            if (curr == head){
                pre = head;
                head = head -> next;
                curr = head;
            }
            // if any other node is to be deleted
            else{
                pre -> next = curr -> next;
                free(curr);
                curr = pre -> next;
            }
        }
        // if current node is not be deleted
        else {
            pre = curr;
            curr = curr -> next;           
        }
    }
    // free the hash table
    free(table);

    return head;
}