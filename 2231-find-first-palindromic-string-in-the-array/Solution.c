// runtime = 23.0ms
// memory usage = 9.4MB

char* firstPalindrome(char** words, int wordsSize) {
    for(int i = 0; i < wordsSize; i++){
        int word_len = strlen(words[i]), is_pallindrome = 1;
        for(int j = 0, k = word_len-1; j <= word_len/2; j++, k--){
            if(words[i][j] != words[i][k]){
                is_pallindrome = 0;
                break;
            }
        }
        if(is_pallindrome){
            return words[i];
        }
    }
    return "";    
}