char* clearDigits(char* s) {
    int len = 0;
    for(int i = 0; i < strlen(s); i++){
        if ((s[i] >= 48) && (s[i] <= 57)){
            len -= 1;
        }
        else{
            s[len++] = s[i];
        }
    }
    s[len] = '\0';
    return s;
}