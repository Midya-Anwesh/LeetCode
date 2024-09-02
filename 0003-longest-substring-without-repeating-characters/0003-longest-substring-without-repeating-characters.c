void _init_arr(int *arr){
    for (int i = 0; i < 128; i++){
        arr[i] = -1;
    }
}

int lengthOfLongestSubstring(char* s) {
    int len = strlen(s), max_len = 0, temp_len = 0;
    int *h_table = (int*)malloc(sizeof(int) * 128);
    _init_arr(h_table);
    for (int i = 0; i < len; i++){
        //char ch = s[i];
        if (h_table[(int)s[i]] == -1){
            temp_len += 1;
            h_table[(int)s[i]] = i;
        }
        else{
            int index = h_table[(int)s[i]], s_i = h_table[(int)s[i]]+1;
            for (int j = 0; j < index; j++){
                if ((s[j] != s[i]) && (h_table[(int)s[j]] < s_i) && (h_table[(int)s[j]] > -1)){
                    h_table[(int)s[j]] = -1;
                    temp_len -= 1;
                }
            }
            h_table[(int)s[i]] = i;
        }
        max_len = (max_len > temp_len)? max_len:temp_len;
    }
    return max_len;
}