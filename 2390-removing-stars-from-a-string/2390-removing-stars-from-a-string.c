char* removeStars(char* s) {
    int len = strlen(s), top = -1;
    char *stack = malloc(sizeof(char)*(len+1));
    for (int i = 0; i < len; i++){
        if (s[i] != '*' || top == -1){
            stack[++top] = s[i];
        }
        else {
            top-=1;
        }
    }
    stack[++top] = '\0';
    return stack;
}