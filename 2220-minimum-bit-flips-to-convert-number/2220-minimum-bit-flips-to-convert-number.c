int minBitFlips(int start, int goal) {
    int count = 0, bit_diff = start^goal;
    while (bit_diff != 0){
        count += bit_diff&1;
        bit_diff >>= 1;
    }
    return count;
}