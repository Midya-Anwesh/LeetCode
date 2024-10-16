/**
 * Note: The returned array must be malloced, assume caller calls free().
 */

int collide(int a, int b){
    return ((a < 0)&(b > 0));
}


int* asteroidCollision(int* asteroids, int asteroidsSize, int* returnSize) {
    int *ret = malloc(sizeof(int) * asteroidsSize);
    *returnSize = -1;
    for (int i = 0; i < asteroidsSize;){
        if (*returnSize == -1){
            ret[++(*returnSize)] = asteroids[i++];
        }
        else if (collide(asteroids[i], ret[*returnSize])){
            if (abs(asteroids[i]) == abs(ret[*returnSize])){
                (*returnSize)--;
                i++;
            }
            else if (abs(asteroids[i]) > abs(ret[*returnSize])){
                (*returnSize)--;
            }
            else{
                i++;
            }
        }
        else{
            ret[++(*returnSize)] = asteroids[i++];
        }
    }
    (*returnSize)++;
    return ret;
}