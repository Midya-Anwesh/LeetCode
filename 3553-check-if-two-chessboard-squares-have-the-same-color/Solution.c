// runtime = 0.0ms
// memory usage = 7.8MB

bool checkTwoChessboards(char* coordinate1, char* coordinate2) {
    return (!(((8-((int)(coordinate1[1])-48)) + (((int)(coordinate1[0]))-97)) % 2) == !(((8-((int)(coordinate2[1])-48)) + (((int)(coordinate2[0]))-97)) % 2));
}