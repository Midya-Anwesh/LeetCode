/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* oddEvenList(struct ListNode* head) {
    if (!head){
        return NULL;
    }
    struct ListNode *oddStart = NULL, *oddEnd = NULL, *evenStart = NULL, *evenEnd = NULL, *curr = head;
    int i = 1;
    while (curr != NULL){
        // Condition for odd
        if (i&1){
            // If first odd node
            if (!oddStart){
                oddStart = curr;
                oddEnd = oddStart;
            }
            // Otherwise add it after oddEnd
            else{
                oddEnd->next = curr;
                oddEnd = oddEnd->next;
            }
        }
        // If it was even
        else{
            // If first even
            if (!evenStart){
                evenStart = curr;
                evenEnd = evenStart;
            }
            // Otherwise add it after evenEnd
            else{
                evenEnd->next = curr;
                evenEnd = evenEnd->next;
            }
        }
        // Move to next node
        curr = curr->next;
        i += 1;
    }

    // If there was no odd node
    if (!oddStart){
        evenEnd->next = NULL;
        return evenStart;
    }
    // If there was no even node
    else if (!evenStart){
        oddEnd->next = NULL;
        return oddStart;
    }
    // If there was both even and odd nodes
    oddEnd->next = evenStart;
    evenEnd->next = NULL;
    return oddStart;
}