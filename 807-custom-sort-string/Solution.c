// runtime = 0.0ms
// memory usage = 5.7MB

char* customSortString(char* order, char* s) {
    int *l_arr = (int*)calloc(26,sizeof(int)), order_len = strlen(order), s_len = strlen(s), sa = 0;
        for (int i = 0; i < s_len; i++){
                l_arr[s[i]-97]++;
                    }
                        for (int i = 0; i < order_len; i++){
                                while(l_arr[order[i]-97]-->0){
                                            s[sa++] = order[i];
                                                    }
                                                        }
                                                            for(int i = 0; i < 26; i++){
                                                                    if(l_arr[i]>0){
                                                                                while(l_arr[i]-->0){
                                                                                                s[sa++] = (char)(i+97);
                                                                                                            }
                                                                                                                    }
                                                                                                                        }
                                                                                                                            free(l_arr);
                                                                                                                                return s;
}