/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */
void flatten(struct TreeNode* root) {
    if (!root){ // If root is NULL return
        return;
    }
    // Recursivly flatten the left subtree
    flatten(root -> left);
    // If we get parent of a leaf node, save pointer to it's right subtree in a verable(temp)
    // Add it's left child to the right pointer, make the left subtree NULL
    struct TreeNode* temp = root -> right;
    root -> right = root -> left;
    root -> left = NULL;
    // Recursively flatten the right sub-tree
    flatten(temp);
    // If there is no right child then add the right-sub tree to the right pointer
    if (!(root -> right)){
        root -> right = temp;
        return;
    }
    // Otherwise find the leaf node of right sub tree and add flattened sub tree to it's right
    struct TreeNode* t2 = root -> right;
    while (t2 && (t2 -> right)){
        t2 = t2 -> right;
    }
    t2 -> right = temp;
}