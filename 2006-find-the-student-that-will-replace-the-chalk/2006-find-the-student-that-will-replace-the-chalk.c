int chalkReplacer(int* chalk, int chalkSize, int k) {
    int sum = 0;
    for (int i = 0; i < chalkSize; i++){
        if ((k-sum) < chalk[i]){
            return i;
        }
        sum += chalk[i];
    }
    k = k%sum;
    sum = 0;
    int ret = -1;
    for (int i = 0; i < chalkSize; i++){
        if ((k-sum) < chalk[i]){
            ret = i;
            break;
        }
        sum += chalk[i];
    }
    return ret;
}