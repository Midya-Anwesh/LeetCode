/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
int gcd(int a, int b){
    if (!b){
        return a;
    }
    return gcd(b, a%b);
}
struct ListNode* insertGreatestCommonDivisors(struct ListNode* head){
    struct ListNode *curr = head, *pre = NULL;
    while ( curr->next != NULL ){
        pre = curr;
        curr = curr->next;
        pre->next = (struct ListNode*)malloc(sizeof(struct ListNode));
        (pre->next)->val = gcd(pre->val, curr->val);
        (pre->next)->next = curr;
    }
    return head;
}