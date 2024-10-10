int pivotIndex(int* nums, int numsSize) {
    if (numsSize == 1){
        return 0;
    }
    int prefix[numsSize+1], postfix[numsSize+1];
    prefix[0] = 0, postfix[numsSize] = 0;
    for (int i = 0; i < numsSize; i++){
        prefix[i+1] = prefix[i]+nums[i];
        postfix[numsSize-i-1] = postfix[numsSize-i]+nums[numsSize-i-1];
    }
    for (int i = 0; i < numsSize; i++){
        if (prefix[i] == postfix[i+1]){
            return i;
        }
    }
    return -1;
}