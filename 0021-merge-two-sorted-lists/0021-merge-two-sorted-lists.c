/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* mergeTwoLists(struct ListNode* list1, struct ListNode* list2) {
    if (!list1 && !list2){
        return NULL;
    }
    struct ListNode **temp = NULL, *head = NULL, *curr = NULL;
    while ((list1 != NULL) && (list2 != NULL)){
        if (list1->val < list2->val){
            temp = &list1;
        }
        else{
            temp = &list2;
        }
        if (head == NULL){
            head = *temp;
            curr = *temp;
        }
        else{
            curr->next = *temp;
            curr = curr->next;
        }
        (*temp) = (*temp)->next;
        curr->next = NULL;
    }
    if (list1 != NULL){
        temp = &list1;       
    }
    else if (list2 != NULL){
        temp = &list2;
    }
    if (!head){
        head = (*temp);
    }
    else{
        curr->next = (*temp);
    }
    return head;
}