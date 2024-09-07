/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */
bool checkSubtree(struct ListNode *head, struct TreeNode *root){
    if (head == NULL){
        return true;
    }
    if ((root == NULL) || ((root->val)!=(head->val))){
        return false;
    }
    return (checkSubtree(head->next, root->left) || checkSubtree(head->next, root->right));
}
bool isSubPath(struct ListNode* head, struct TreeNode* root) {
    struct TreeNode **queue = (struct TreeNode**)malloc(sizeof(struct TreeNode*)*2501);
    int front = 0, rear = -1;
    queue[++rear] = root;
    while (front <= rear){
        struct TreeNode *curr = queue[front++];
        if ((curr -> val) == (head->val)){
            if (checkSubtree(head->next, curr->left) || checkSubtree(head->next, curr->right)){
                return true;
            }
        }
        if ((curr -> left) != NULL){
            queue[++rear] = curr -> left;
        }
        if ((curr->right) != NULL){
            queue[++rear] = curr -> right;
        }
    }
    free(queue);
    return false;
}