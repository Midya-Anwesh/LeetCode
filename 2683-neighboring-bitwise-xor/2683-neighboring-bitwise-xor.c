/*
    1. As shown in the example 1, derived[0] = original[0] ^ original[1]
    2. We can rewrite it as, original[1] = original[0] ^ derived[0]

    Now, we will check for validity for original[0] as 0 and 1
    First consider original[0] = 0
    1. original[i] = original[i-1] ^ derived[i-1], for i in range(1, derivedSize)
    2. now check if derived[derivedSize-1] = original[0] ^ original[derivedSize-1]
    3. Do, sbove two steps for original[0] = 1 also
*/
#pragma GCC optimize("O3", "loop-unroll")
bool helper(int *derived, int derivedSize, int original0){
    int start = original0, end = original0;

    for (int i = 1; i < derivedSize; i++){
        end = derived[i-1] ^ end;
    }

    return derived[derivedSize-1] == start ^ end;
}

bool doesValidArrayExist(int* derived, int derivedSize) {
    return helper(derived, derivedSize, 0) | helper(derived, derivedSize, 1);
}