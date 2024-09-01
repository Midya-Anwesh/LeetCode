// runtime = 6.0ms
// memory usage = 7.6MB

int minimumLength(char* s) {
    int len = strlen(s);
        int start = 0, end = len-1;
            while(start<end){
                    if(s[start]==s[end]){
                                if(s[start]==s[start+1]){
                                                while(s[start]==s[start+1]){
                                                                    start++;
                                                                                        if(start==end){
                                                                                                                return 0;
                                                                                                                                    }
                                                                                                                                                    }
                                                                                                                                                                }
                                                                                                                                                                            while(s[start]==s[end]){
                                                                                                                                                                                            end--;
                                                                                                                                                                                                            if(start==end){
                                                                                                                                                                                                                                return 0;
                                                                                                                                                                                                                                                }
                                                                                                                                                                                                                                                            }
                                                                                                                                                                                                                                                                        start++;
                                                                                                                                                                                                                                                                                    if(start == end){
                                                                                                                                                                                                                                                                                                    return 1;
                                                                                                                                                                                                                                                                                                                }
                                                                                                                                                                                                                                                                                                                        }
                                                                                                                                                                                                                                                                                                                                else{
                                                                                                                                                                                                                                                                                                                                            break;
                                                                                                                                                                                                                                                                                                                                                    }
                                                                                                                                                                                                                                                                                                                                                        }
                                                                                                                                                                                                                                                                                                                                                            return end-start+1;
}