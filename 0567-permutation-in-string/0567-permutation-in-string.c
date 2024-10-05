int *hash(char *s, int start, int end){
    int *table = (int*)calloc(sizeof(int), 26);
    for (int i = start; i <= end; i++){
        table[s[i]-97] += 1;
    }
    return table;
}
bool isSame(int *table1, int *table2){
    for (int i = 0; i < 26; i++){
        if (table1[i] && table1[i] != table2[i]){
            return false;
        }
    }
    return true;
}
bool checkInclusion(char* s1, char* s2) {
    int len1 = strlen(s1), len2 = strlen(s2);
    if (len1 > len2){
        return false;
    }
    int *hs1 = hash(s1, 0, len1-1);
    int window_start = 0, window_end = len1-1;
    int *hs2 = hash(s2, window_start, window_end);
    while (window_end < len2){
        if ( isSame(hs1, hs2) ){
            free(hs1);
            free(hs2);
            return true;
        }
        hs2[s2[window_start++]-97] -= 1;
        if (window_end == len2-1){
            break;
        }
        hs2[s2[++window_end]-97] += 1;
    }
    free(hs1);
    free(hs2);
    return false;
}