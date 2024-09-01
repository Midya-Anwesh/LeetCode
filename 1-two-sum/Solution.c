// runtime = 238.0ms
// memory usage = 6.4MB

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* twoSum(int* nums, int numsSize, int target, int* returnSize) {
    int *ans = (int*)calloc(sizeof(int),2);
    *returnSize = 2;
    for(int i = 0; i < numsSize; i++) {       
       


        for(int j = 0; j < numsSize; j++){
            if(j == i){
                continue;
           }
            else if(nums[i]+nums[j]==target){
                ans[0]=i;
                ans[1]=j;
                return ans;
            }
        }
    }
    return ans;    

}