int *bitSet;

int addToBitSet(int num){
    int or = 0;
    for (int i = 0; i < 32; i++){
        bitSet[i] += num&1;
        or |= ((bitSet[i] > 0)? 1:0) << i;
        num >>= 1;
    }
    return or;
}

int subFromBitSet(int num){
    int or = 0;
    for (int i = 0; i < 32; i++){
        bitSet[i] -= num&1;
        or |= ((bitSet[i] > 0)? 1:0) << i;
        num >>= 1;
    }
    return or;
}

int minimumSubarrayLength(int* nums, int numsSize, int k) {
    if (!k){
        return (numsSize > 0)? 1:-1;
    }
    bitSet = calloc(32, sizeof(int));
    int st = 0, end = 0, or = 0, ret = INT_MAX, flag = 0;
    while (end < numsSize){
        or = addToBitSet(nums[end]);
        if (or >= k){
            ret = (ret < (end-st+1))? ret:(end-st+1);
            flag = 1;
            while ((or >= k) && (st < end)){
                or = subFromBitSet(nums[st]);
                st += 1;
            }
            if (or >= k){
                ret = (ret < (end-st+1))? ret:(end-st+1);
            }
            else{
                st -= 1;
                or = addToBitSet(nums[st]);
                ret = (ret < (end-st+1))? ret:(end-st+1);
            }
        }
        end += 1;
    }
    return (flag)? ret:-1;
}