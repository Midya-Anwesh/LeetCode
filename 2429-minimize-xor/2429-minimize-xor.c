int minimizeXor(int num1, int num2) {
    int setBitCount1 = 0, setBitCount2 = 0, temp1 = num1, temp2 = num2;
    // Count how many set bits num1 has
    while (temp1){
        setBitCount1 += temp1&1;
        temp1 >>= 1;
    }
    // Count how many set bits num2 has
    while (temp2){
        setBitCount2 += temp2&1;
        temp2 >>= 1;
    }
    // If both have different number of set bits
    while (setBitCount1 != setBitCount2){
        // If num2 has less set bits
        // Unset the rightmost set bit of num1
        if (setBitCount2 < setBitCount1){
            num1 &= num1 - 1;
            setBitCount1 -= 1;
        }
        // If num2 has more set bits
        // Set the rightmost unset bit of num1
        else{
            num1 |= num1 + 1;
            setBitCount2 -= 1;
        }
        // Doning so will result less xor value
    }
    return num1;
}