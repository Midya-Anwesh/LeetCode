// runtime = 0.0ms
// memory usage = 5.8MB

/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* rotateRight(struct ListNode* head, int k) {
    if(head == NULL){
        return head;
    }
    int len = 0;
    for(struct ListNode *temp = head; temp!= NULL; temp=temp->next,len++);
    printf("%d",len);
    if(k%len==0){

        return head;
    }
    struct ListNode *temp = head, *tail = NULL;
    for(;temp->next!=NULL;temp=temp->next);
    tail = temp;
    temp = head;
    tail->next = head;
    if(k%len==1){
        head = tail;
        for(;temp->next!=head;temp=temp->next);
        temp->next = NULL;
        return head;
    }
    int to_rotate = k%len;
    for(int i = 0; i < len-to_rotate-1; temp = temp-> next, i++);
    tail = temp->next;
    //temp = head;
    head = tail;


    temp->next = NULL;
    return head;
}