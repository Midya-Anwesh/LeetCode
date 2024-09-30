
typedef struct DoublyListNode{
    struct DoublyListNode *prev;
    int val;
    struct DoublyListNode *next;
} DoublyListNode;

typedef struct {
    DoublyListNode *bottom, *top;
    int maxSize;
    int len;
} CustomStack;


CustomStack* customStackCreate(int maxSize) {
    CustomStack *obj = calloc(sizeof(CustomStack), 1);
    obj->maxSize = maxSize;
    return obj;
}

void customStackPush(CustomStack* obj, int x) {
    if (obj->len == obj->maxSize){
        return;
    }
    if (!obj->bottom){
        obj->bottom = calloc(sizeof(DoublyListNode), 1);
        obj->bottom->val = x;
        obj->top = obj->bottom;
    }
    else{
        DoublyListNode *temp = obj->top;
        obj->top->next = calloc(sizeof(DoublyListNode), 1);
        obj->top = obj->top->next;
        obj->top->prev = temp;
        obj->top->val = x;
    }
    obj->len += 1;
}

int customStackPop(CustomStack* obj) {
    int ret = -1;
    if (obj->top){
        if (obj->top == obj->bottom){
            ret = obj->top->val;
            free(obj->top);
            obj->bottom = NULL;
            obj->top = NULL;
        }
        else{
            ret = obj->top->val;
            obj->top = obj->top->prev;
            free(obj->top->next);
            obj->top->next = NULL;
        }
        obj->len -= 1;
    }
    return ret;
}

void customStackIncrement(CustomStack* obj, int k, int val) {
    DoublyListNode *temp = obj->bottom;
    for (int i = 0; i < k && temp; i++){
        temp->val += val;
        temp = temp->next;
    }
}

void customStackFree(CustomStack* obj) {
    while(obj->bottom){
        DoublyListNode *temp = obj->bottom;
        obj->bottom = obj->bottom->next;
        free(temp);
    }
    free(obj);
}

/**
 * Your CustomStack struct will be instantiated and called as such:
 * CustomStack* obj = customStackCreate(maxSize);
 * customStackPush(obj, x);
 
 * int param_2 = customStackPop(obj);
 
 * customStackIncrement(obj, k, val);
 
 * customStackFree(obj);
*/