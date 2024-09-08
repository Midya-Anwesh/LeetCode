/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int countNodes(struct ListNode *head){
    int count = 0;
    for (;head!=NULL; count++, head = head->next);
    return count;
}
struct ListNode** splitListToParts(struct ListNode* head, int k, int* returnSize) {
    int len = countNodes(head);
    struct ListNode **parts = (struct ListNode **)calloc(sizeof(struct ListNode *), k);
    
    for (int i = 0; i < k; i++){
        
        int sub_part_len = (len/k)+((i < len%k)? 1:0);
        if (!sub_part_len){
            break;
        }
        
        parts[i] = (struct ListNode *)calloc(sizeof(struct ListNode), sub_part_len);
        for (int j = 0; j < sub_part_len; j++){
            
            parts[i][j] = (*head);
            struct ListNode *temp = head;
            head = head->next;
            if (j == sub_part_len-1){
                temp -> next = NULL;
                parts[i][j].next = NULL;
            }
            
            
        }
        
    }
    *returnSize = k;
    return parts;
}