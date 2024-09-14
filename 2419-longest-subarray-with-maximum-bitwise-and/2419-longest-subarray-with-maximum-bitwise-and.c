int longestSubarray(int* nums, int numsSize) {
    int max = nums[0], count = 1, temp_count = 1;
    for (int i = 1; i < numsSize; i++){
        if (nums[i] > max){
            max = nums[i];
            count = 1;
            temp_count = 1;
        }
        else if (nums[i] == max){
            temp_count += 1;
        }
        else{
            count = (temp_count > count)? temp_count:count;
            temp_count = 0;
        }
    }
    
    return (temp_count > count)? temp_count:count;
}