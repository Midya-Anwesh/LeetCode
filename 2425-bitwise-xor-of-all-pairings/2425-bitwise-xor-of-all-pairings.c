int xorAllNums(int* nums1, int nums1Size, int* nums2, int nums2Size) {
    // If both the arrays are even
    if ( (!(nums1Size&1)) && (!(nums2Size&1)) ){
        return 0;
    }

    // Return variable
    int ret = 0;

    // If nums1 is even and nums2 is odd
    if (!(nums1Size&1)){
        for (int i = 0; i < nums1Size; i++){
            ret ^= nums1[i];
        }
        return ret;
    }

    // If nums2 is even and nums1 is odd
    if (!(nums2Size&1)){
        for (int i = 0; i < nums2Size; i++){
            ret ^= nums2[i];
        }
        return ret;
    }

    // If both array are odd
    for (int i = 0; i < nums1Size; i++){
        ret ^= nums1[i];
    }
    for (int i = 0; i < nums2Size; i++){
        ret ^= nums2[i];
    }
    return ret;
}