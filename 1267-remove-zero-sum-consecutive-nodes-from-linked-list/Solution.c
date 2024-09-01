// runtime = 4.0ms
// memory usage = 7.3MB

/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */


struct ListNode* removeZeroSumSublists(struct ListNode* head) {
    if(head -> next == NULL && head -> val == 0){
        return NULL;
    }
    int *arr = malloc(1000*sizeof(int));
    int end = -1;
    struct ListNode *temp = head;
    while(temp != NULL){
        if(temp -> val == 0){
            temp = temp -> next;
            continue;
        }
        int sum = temp -> val, skip = 0;
        for(int i = end; i >= 0; i--){
            sum += arr[i];
            if(sum == 0){
                end = i-1;
                skip = 1;
                break;
            }
        }
        if(!skip){
        arr[++end] = temp -> val;
        }
        temp = temp -> next;
    }
    if(end == -1){
        while(head != NULL){
            temp = head;
            head = temp->next;
            free(temp);
        }
        return NULL;
    }
    temp = head;
    for(int i = 0; i <= end; i++){
        temp -> val = arr[i];
        if(i < end){
        temp = temp->next;
        }
    }
    if(temp->next == NULL){
        return head;
    }
    struct ListNode *p = temp;
    temp = temp->next;
    p->next = NULL;
    while(temp != NULL){
        p = temp;
        temp = temp->next;
        free(p);
    }
    return head;
}