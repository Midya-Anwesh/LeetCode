int largestAltitude(int* gain, int gainSize) {
    int ret = 0, temp = 0;
    for (int i = 0; i < gainSize; i++){
        temp += gain[i];
        ret = (ret > temp)? ret:temp;
    }
    return ret;
}