/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */

void reverse(struct ListNode **head){
    struct ListNode *curr = *head;
    while (curr && curr->next){
        int val = curr->val;
        curr->val = curr->next->val;
        curr->next->val = val;
        curr = curr->next->next;
    }
}

struct ListNode* swapPairs(struct ListNode* head) {
    reverse(&head);
    return head;
}