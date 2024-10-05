int *hash(char *s){
    int len = strlen(s);
    int *table = calloc(sizeof(int), 26);
    for (int i = 0 ; i < len; i++){
        table[s[i]-97] += 1;
    }
    return table;
}
bool isAnagram(char* s, char* t) {
    int *strhash = hash(s), *thash = hash(t);
    for (int i = 0; i < 26; i++){
        if (strhash[i] && strhash[i] != thash[i]){
            return false;
        }
    }
    return true;
}