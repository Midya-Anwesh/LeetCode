
/*typedef struct ListNode{
    int val;
    struct ListNode *next;
}*/

typedef struct Queue {
    int maxSize, currSize;
    struct ListNode *front, *rear;
} MyCircularQueue;


MyCircularQueue* myCircularQueueCreate(int k) {
    struct Queue *obj = (struct Queue*) calloc(sizeof(struct Queue), 1);
    obj -> maxSize = k;
    return obj;
}

bool myCircularQueueEnQueue(MyCircularQueue* obj, int value) {
    // If possible to add a new value
    if ((obj -> currSize) < (obj -> maxSize)){
        // Create a new node with specified value
        struct ListNode *newNode = calloc(sizeof(struct ListNode), 1);
        newNode -> val = value;
        newNode -> next = NULL;
        // If it's first node
        if (obj->front == NULL){
            obj -> front = newNode;
            obj -> rear = newNode;
        }
        // Otherwise append it after last node
        else{
            obj -> rear -> next = newNode;
            obj -> rear = obj -> rear -> next;
        }
        // Increment curr length of obj
        obj -> currSize = (obj -> currSize) + 1;
        return true;
    }
    // If it's not possible to add
    return false;
}

bool myCircularQueueDeQueue(MyCircularQueue* obj) {
    // If obj is empty
    if (! (obj -> front) ){
        return false;
    }
    // Else if it is the last element
    else if ((obj -> front) == (obj -> rear)){
        obj -> rear = NULL;
    }
    // Otherwise return value of front and remove it
    struct ListNode *temp = obj -> front -> next;
    free(obj -> front);
    obj -> front = temp;
    (obj -> currSize) = (obj -> currSize) - 1;
    return true;
}

int myCircularQueueFront(MyCircularQueue* obj) {
    if (!(obj -> front)){
        return -1;
    }
    return obj -> front -> val;
}

int myCircularQueueRear(MyCircularQueue* obj) {
    if (!(obj -> rear)){
        return -1;
    }
    return obj -> rear -> val;
}

bool myCircularQueueIsEmpty(MyCircularQueue* obj) {
    return (obj -> currSize) == 0;
}

bool myCircularQueueIsFull(MyCircularQueue* obj) {
    return (obj -> currSize) == (obj -> maxSize);
}

void myCircularQueueFree(MyCircularQueue* obj) {
    // Free the linked list
    while (obj -> front != NULL){
        struct ListNode *temp = obj -> front -> next;
        free(obj -> front);
        obj -> front = temp;
    }
    // Free the object
    free(obj);
}

/**
 * Your MyCircularQueue struct will be instantiated and called as such:
 * MyCircularQueue* obj = myCircularQueueCreate(k);
 * bool param_1 = myCircularQueueEnQueue(obj, value);
 
 * bool param_2 = myCircularQueueDeQueue(obj);
 
 * int param_3 = myCircularQueueFront(obj);
 
 * int param_4 = myCircularQueueRear(obj);
 
 * bool param_5 = myCircularQueueIsEmpty(obj);
 
 * bool param_6 = myCircularQueueIsFull(obj);
 
 * myCircularQueueFree(obj);
*/