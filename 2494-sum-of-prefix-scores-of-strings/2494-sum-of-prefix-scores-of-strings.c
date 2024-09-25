/**
 * Note: The returned array must be malloced, assume caller calls free().
 */

typedef struct TrieNode {
    int cnt;
    struct TrieNode* child[26];
} Node;
void init(Node* root) {
    root->cnt = 0;
    for (int i = 0; i < 26; i++)
        root->child[i] = NULL;
}
void freeNode(Node* root) {
    for (int i = 0; i < 26; ++i)
        free(root->child[i]);
    free(root);
    return;
}

int* sumPrefixScores(char** words, int wordsSize, int* returnSize) {
    Node* root = NULL;
    Node* curr = NULL;
    char* word = NULL;
    int* ret = NULL;
    int subAns = 0;
    int idx = 0;
    int wordSize = 0;

    *returnSize = wordsSize;
    ret = (int*)malloc(sizeof(int) * wordsSize);
    if (ret == NULL) {
        goto END;
    }
    memset(ret, 0, sizeof(int) * wordsSize);

    root = (Node*)malloc(sizeof(Node));
    if (root == NULL) {
        goto END;
    }
    init(root);

    for (int i = 0; i < wordsSize; i++) {
        curr = root;
        word = words[i];
        wordSize = strlen(word);

        for (int j = 0; j < wordSize; j++) {
            idx = word[j] - 'a';

            if (curr->child[idx] == NULL) {
                curr->child[idx] = (Node*)malloc(sizeof(Node));
                if (curr->child[idx] == NULL) {
                    goto FREE;
                }
                init(curr->child[idx]);
            }

            curr = curr->child[idx];
            curr->cnt += 1;
        }
    }

    for (int i = 0; i < wordsSize; i++) {
        subAns = 0;
        curr = root;
        word = words[i];
        wordSize = strlen(word);

        for (int j = 0; j < wordSize; j++) {
            idx = word[j] - 'a';
            curr = curr->child[idx];
            subAns += curr->cnt;
        }

        ret[i] = subAns;
    }

FREE:
    freeNode(root);
END:
    return ret;
}