/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */
void flatten(struct TreeNode* root) {
    if (!root){
        return;
    }
    flatten(root -> left);
    struct TreeNode* temp = root -> right;
    root -> right = root -> left;
    root -> left = NULL;
    flatten(temp);
    if (!(root -> right)){
        root -> right = temp;
        return;
    }
    struct TreeNode* t2 = root -> right;
    while (t2 && (t2 -> right)){
        t2 = t2 -> right;
    }
    t2 -> right = temp;
}