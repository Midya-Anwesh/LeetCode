/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* xorQueries(int* arr, int arrSize, int** queries, int queriesSize, int* queriesColSize, int* returnSize) {
    int *ret = malloc(sizeof(int)*queriesSize), *xor_arr = calloc(sizeof(int), arrSize+1);
    for (int i = 0; i < arrSize; i++){
        xor_arr[i+1] = xor_arr[i]^arr[i];
    }
    for (int i = 0; i < queriesSize; i++){
        ret[i] = xor_arr[queries[i][0]]^xor_arr[queries[i][1]]^arr[queries[i][1]];
    }
    *returnSize = queriesSize;
    return ret;
}