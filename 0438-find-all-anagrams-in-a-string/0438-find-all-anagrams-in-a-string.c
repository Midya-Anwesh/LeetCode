/**
 * Note: The returned array must be malloced, assume caller calls free().
 */

bool isAnagram(int *t1, int *t2){
    for (int i = 0; i < 26; i++){
        if (t1[i] && t1[i]!=t2[i]){
            return false;
        }
    }
    return true;
}

int *hash(char *s, int start, int end){
    int *table = calloc(sizeof(int), 26);
    for (int i = start; i <= end; i++){
        table[s[i]-97] += 1;
    }
    return table;
}

int* findAnagrams(char* s, char* p, int* returnSize) {
    int slen = strlen(s), plen = strlen(p);
    *returnSize = 0;
    if (plen > slen){
        return calloc(sizeof(int), 0);
    }
    int *start_indices = calloc(sizeof(int), slen);
    int window_start = 0, window_end = plen-1;
    int *phash = hash(p, 0, plen-1), *shash = hash(s, window_start, window_end);
    while (1){
        if ( isAnagram(phash, shash) ){
            start_indices[(*returnSize)++] = window_start;
        }
        if (window_end == slen-1){
            break;
        }
        shash[s[window_start++]-97] -= 1;
        shash[s[++window_end]-97] += 1;
    }
    return start_indices;
}