typedef struct Trie{
    struct Trie *child[26];
    int wordEnd;
}Trie;

void insertSubStr(Trie **root, char *s, int st, int end){
    if (*root == NULL){
        (*root) = calloc(sizeof(Trie), 1);
    }
    Trie *temp = *root;
    while (st <= end){
        if (temp->child[s[st]-97] == NULL){
            temp->child[s[st]-97] = calloc(sizeof(Trie), 1);
        }
        temp = temp->child[s[st]-97];
        st += 1;
    }
    temp -> wordEnd = 1;
}

void removeSubStr(Trie **root, char *s, int st, int end){
    if (*root == NULL){
        return;
    }
    Trie *temp = *root;
    while (st <= end){
        if (temp -> child[s[st]-97] == NULL){
            return;
        }
        temp = temp->child[s[st]-97];
        st += 1;
    }
    temp -> wordEnd = 0;
}

int exists(Trie *root, char *s, int st, int end){
    if (root == NULL){
        return 0;
    }
    while (st <= end){
        if (root->child[s[st]-97] == NULL){
            return 0;
        }
        root = root->child[s[st]-97];
        st += 1;
    }
    return root -> wordEnd;
}

void splitAndCount(Trie **root, char *s, int st, int len, int curr, int *count){
    if (st == len){
        *count = ((*count) > curr)? (*count):curr;
        return;
    }
    for (int i = st; i < len; i++){
        if (!exists(*root, s, st, i)){
            insertSubStr(root, s, st, i);
            splitAndCount(root, s, i+1, len, curr+1, count);
            removeSubStr(root, s, st, i);
        }
    }
}

int maxUniqueSplit(char* s) {
    Trie *root = NULL;
    int ret = 0;
    splitAndCount(&root, s, 0, strlen(s), 0, &ret);
    return ret;
}