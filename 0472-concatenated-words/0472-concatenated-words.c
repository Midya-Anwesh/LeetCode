/**
 * Note: The returned array must be malloced, assume caller calls free().
 */

typedef struct Trie{
    struct Trie *child[26];
    int wordEnd;
}TrieNode;

int concated(TrieNode *root, char *s, int index, int len){
    if (root == NULL){
        return 0;
    }
    TrieNode *temp = root;
    while (index < len){
        if (temp -> child[s[index]-97] == NULL){
            return 0;
        }
        temp = temp->child[s[index]-97];
        index += 1;
        if (temp -> wordEnd){
            if (index >= len){
                return 1;
            }
            if (concated(root, s, index, len)){
                return 1;
            }
        }
    }
    return 0;
}

void addWord(TrieNode **root, char *s, int len){
    if (*root == NULL){
        (*root) = calloc(sizeof(TrieNode), 1);
    }
    TrieNode *temp = *root;
    for (int i = 0; i < len; i++){
        if (temp->child[s[i]-97] == NULL){
            temp->child[s[i]-97] = calloc(sizeof(TrieNode), 1);
        }
        temp = temp->child[s[i]-97];
    }
    temp->wordEnd = 1;
}

int compare(const void *one, const void *two) {
    const char *iOne = *(const char * const *)one;
    const char *iTwo = *(const char * const *)two;
    size_t len1 = strlen(iOne);
    size_t len2 = strlen(iTwo);
    if (len1 > len2)
        return 1;
    if (len2 > len1)
        return -1;
    return strcmp(iOne, iTwo);
}

char** findAllConcatenatedWordsInADict(char** words, int wordsSize, int* returnSize) {
    qsort(words, wordsSize, sizeof(char*), compare);
    char **ret = malloc(sizeof(char*) * wordsSize);
    *returnSize = 0;
    TrieNode *root = NULL;
    for (int i = 0; i < wordsSize; i++){
        int len = strlen(words[i]);
        if (concated(root, words[i], 0, len)){
            ret[(*returnSize)++] = words[i];
        }
        else{
            addWord(&root, words[i], len);
        }
    }
    return ret;
}