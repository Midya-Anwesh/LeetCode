// runtime = 0.0ms
// memory usage = 5.6MB

char * mergeAlternately(char * word1, char * word2){
    int len = strlen(word1) + strlen(word2) + 1;
    char *merged_arr = (char*)malloc(len * sizeof(char) );
    int index = 0, i = 0, j = 0;
    while (word1[i]!='\0' && word2[j]!='\0'){
        if(index % 2 == 0){
            merged_arr[index++] = word1[i++];
        }
        else{
            merged_arr[index++] = word2[j++];
        }
    }
    while(word1[i] != '\0'){
        merged_arr[index++] = word1[i++];
    }
    while(word2[j] != '\0'){
        merged_arr[index++] = word2[j++];
    }
    merged_arr[index] = '\0';
    return merged_arr;
}