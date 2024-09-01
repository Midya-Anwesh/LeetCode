// runtime = 88.0ms
// memory usage = 19.3MB

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* productExceptSelf(int* nums, int numsSize, int* returnSize) {
     *returnSize = numsSize;
         int *pm = (int*)malloc(numsSize*sizeof(int)), *result = (int*)malloc(numsSize*sizeof(int));
             pm[0] = nums[0];
                 for(int i = 1; i < numsSize; i++){
                         pm[i] = pm[i-1]*nums[i];
                             }
                                 for(int i = numsSize-2; i >= 0; i--){
                                         nums[i] = nums[i]*nums[i+1];
                                             }
                                                 result[0]=nums[1];
                                                     result[numsSize-1]=pm[numsSize-2];
                                                         for(int i = 1; i < numsSize-1; i++){
                                                                 result[i] = pm[i-1] * nums[i+1];
                                                                     }
                                                                         free(pm);
                                                                             return result;
}