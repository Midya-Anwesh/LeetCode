/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* modifiedList(int* nums, int numsSize, struct ListNode* head) {
    int *table = (int *)calloc(sizeof(int), 100001);
    for (int i = 0; i < numsSize; table[nums[i++]]++);

    struct ListNode *pre = NULL, *curr = head;

    while (curr != NULL){
        if ( table[(curr -> val)] ){
            if (curr == head){
                pre = head;
                head = head -> next;
                curr = head;
            }
            else{
                pre -> next = curr -> next;
                free(curr);
                curr = pre -> next;
            }
        }

        else {
            pre = curr;
            curr = curr -> next;           
        }
    }

    free(table);

    return head;
}