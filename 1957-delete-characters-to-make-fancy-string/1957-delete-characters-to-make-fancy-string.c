char* makeFancyString(char* s) {
    int top = -1, count = 0, len = strlen(s);
    for (int i = 0; i < len; i++){
        if (top == -1){
            s[++top] = s[i];
        }
        else{
            if (s[top] == s[i]){
                if (count++ < 1){
                    s[++top] = s[i];
                }
            }
            else{
                s[++top] = s[i];
                count = 0;
            }
        }
    }
    s[++top] = '\0';
    return s;
}