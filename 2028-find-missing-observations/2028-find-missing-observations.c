/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* missingRolls(int* rolls, int rollsSize, int mean, int n, int* returnSize) {
    int sum = 0;
    for (int i = 0; i < rollsSize; sum+=rolls[i++]);

    int to_divide = (mean*(rollsSize+n))-sum;

    if ( (to_divide > 6*n) || (to_divide < n) ){
        *returnSize = 0;
        return NULL;
    }

    int base = to_divide/n, increment = to_divide%n;

    int *ret = (int *)malloc(sizeof(int)*n);
    for (int i = 0; i < n; ret[i++] = (base+((i<increment)? 1:0)));
    *returnSize = n;
        
    return ret;
}