#pragma GCC optimize("loop-unroll")
int valid(char *nums, int numsSize, int index, int curr, int target){
    if (index >= numsSize){ // If all characters from string is used
        if (curr == target){ // If using all characters we get target sum, success
            return 1;
        }
        return 0;
    }
    // Temporary string to store current partition of the string
    char currPart[8];
    memset(currPart, '\0', 8);
    // Check validity recursively for all indices
    for (int i = index; i < numsSize; i++){
        strncat(currPart, &nums[i], 1);
        if (valid(nums, numsSize, i+1, curr+atoi(currPart), target)){
            return 1;
        }
    }
    return 0;
}

int punishmentNumber(int n) {
    int ret = 0;
    for (int i = 1; i <= n; i++){
        int num = i*i;
        if ((num % 9) > 1){ // Early stopping
            continue;
        }
        // Convert the square into string
        int temp = num, size = floor(log10(num)) + 1;
        char nums[size];
        int index = size-1;
        while (temp){
            nums[index--] = (temp%10) + 48;
            temp /= 10;
        }
        // Recursive function to check validity
        if (valid(nums, size, 0, 0, i)){
            ret += num;
        }
    }
    return ret;
}