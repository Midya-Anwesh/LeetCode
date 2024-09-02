void _init_arr(int *arr){
    for (int i = 0; i < 128; i++){
        arr[i] = -1;
    }
}

int lengthOfLongestSubstring(char* s) {
    int len = strlen(s), max_len = 0, left_idx = 0;
    int *charIndex = (int*)malloc(sizeof(int) * 128);
    _init_arr(charIndex);

    for (int right_idx = 0; right_idx < len; right_idx++){
        if (charIndex[s[right_idx]] >= left_idx){
            left_idx = charIndex[s[right_idx]]+1;
        }
        charIndex[s[right_idx]] = right_idx;
        int curr_len = right_idx - left_idx + 1;
        max_len = (max_len > curr_len)? max_len:curr_len;
    }
    
    return max_len;
}