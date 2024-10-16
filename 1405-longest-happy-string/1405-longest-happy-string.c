int max(int *arr){ //a = arr[0], b = arr[1], c = arr[2]
    return (arr[0] > arr[1]) ? (arr[0] > arr[2] ? arr[0] : arr[2]) : (arr[1] > arr[2] ? arr[1] : arr[2]);
}

int possible(int *arr, int *index, char *s, int len, int *to_repeat){
    if ((arr[0]|arr[1]|arr[2]) == 0){
        return 0;
    }
    int m = max(arr);
    if (len == -1){
        while (arr[*index] != m){
            *index = ((*index)+1)%3;
        }
        *to_repeat = (m > 2)? 2:m;
        return 1;
    }
    for (int i = 0; i < 3; i++){
        if ((arr[i] == m) && (i != s[len]-97)){
            *index = i;
            *to_repeat = (m > 2)? 2:m;
            return 1;
        }
    }
    for (int i = 0; i < 3; i++){
        if ((i != s[len]-97) && arr[i]){
            *index = i;
            *to_repeat = 1;
            return 1;
        }
    }
    return 0;
}

char* longestDiverseString(int a, int b, int c) {
    int arr[] = {a, b, c}, index = 0, to_repeat = 0, i = 0;
    char *ret = (char*)malloc(sizeof(char)*1000);
    while (possible(arr, &index, ret, i-1, &to_repeat)){
        // int to_repeat = (arr[index] > 2)? 2:arr[index];
        arr[index] -= to_repeat;
        while (to_repeat-- > 0){
            ret[i++] = (char)(index+97);
        }
    }
    ret[i] = '\0';
    return ret;
}