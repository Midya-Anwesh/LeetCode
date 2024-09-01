// runtime = 96.0ms
// memory usage = 32.8MB

/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */


struct ListNode* mergeInBetween(struct ListNode* list1, int a, int b, struct ListNode* list2){
    struct ListNode *insert, *end = NULL, *temp = list1, *temp1 = list2, *connect = NULL;
    for(int i = 0; end == NULL || connect == NULL; i++){
        if (i == a-1){
            insert = temp;
        }
        else if (i == b+1){
            end = temp;
        }
        if (temp1->next!=NULL){
            temp1=temp1->next;
            if(temp1->next==NULL){
                connect = temp1;
            }
        }
        if (temp->next!=NULL)
        temp = temp->next;


    }
    insert->next = list2;
    connect->next = end;
    return list1;


}