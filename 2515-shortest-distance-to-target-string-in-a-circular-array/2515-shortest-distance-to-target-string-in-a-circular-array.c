int closetTarget(char** words, int wordsSize, char* target, int startIndex) {
    if (!strcmp(words[startIndex], target)){
        return 0;
    }

    int forward_offset = 1, backward_offset = 1;
    for (int i = 0; i < wordsSize; i++){

        int forward_index = (startIndex + forward_offset) % wordsSize;
        int backward_index = (wordsSize + startIndex - backward_offset) % wordsSize;

        if (!strcmp(words[forward_index], target)){
            return forward_offset;
        }
        else if (!strcmp(words[backward_index], target)){
            return backward_offset;
        }
    }

    return -1;
}