// runtime = 17.0ms
// memory usage = 7.5MB

/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* addTwoNumbers(struct ListNode* l1, struct ListNode* l2) {
    struct ListNode* ans = NULL, *tail = NULL, *n = NULL;
    int carry=0;
    for(;l1!=NULL && l2!= NULL;){
        struct ListNode *new_node = malloc(sizeof(struct ListNode));
        int t = l1->val + l2->val + carry;
        new_node -> val = t%10;
        new_node -> next = NULL;
        if(ans == NULL){
            ans = new_node;
            tail = new_node;
        }
        else{
            tail->next = new_node;
            tail = tail->next;
        }
        carry = t/10;
        l1=l1->next;
        l2=l2->next;
    }
    if(l1!=NULL){
        n = l1;
    }
    else{
        n = l2;
    }
    while(n!=NULL){
        struct ListNode *new_node=malloc(sizeof(struct ListNode));
        new_node -> next = NULL;
        int t = n->val + carry;
        new_node -> val = t%10;
        carry = t/10;
        tail->next = new_node;
        tail = tail->next;
        n = n->next;
    }
    if(carry){
        struct ListNode *new_node = malloc(sizeof(struct ListNode));
        new_node -> val = carry;
        new_node -> next = NULL;
        tail -> next = new_node;
    }
    return ans;
    
}