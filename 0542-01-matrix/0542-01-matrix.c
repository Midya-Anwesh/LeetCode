/**
 * Return an array of arrays of size *returnSize.
 * The sizes of the arrays are returned as *returnColumnSizes array.
 * Note: Both returned array and *columnSizes array must be malloced, assume caller calls free().
 */

void normalize(int **mat, int rowNo, int colNo, int row, int col){
    /* check if any adjacent cells can be normalized or not
    if yes then normalize it furthur*/
    if (row > 0 && mat[row-1][col] > mat[row][col]+1){
        mat[row-1][col] = mat[row][col]+1;
        normalize(mat, rowNo, colNo, row-1, col);
    }
    if (row < rowNo-1 && mat[row+1][col] > mat[row][col]+1){
        mat[row+1][col] = mat[row][col]+1;
        normalize(mat, rowNo, colNo, row+1, col);
    }
    if (col > 0 && mat[row][col-1] > mat[row][col]+1){
        mat[row][col-1] = mat[row][col]+1;
        normalize(mat, rowNo, colNo, row, col-1);
    }
    if (col < colNo-1 && mat[row][col+1] > mat[row][col]+1){
        mat[row][col+1] = mat[row][col]+1;
        normalize(mat, rowNo, colNo, row, col+1);
    }
}


int** updateMatrix(int** mat, int matSize, int* matColSize, int* returnSize, int** returnColumnSizes) {
    int **ret = malloc(sizeof(int*)*matSize);
    (*returnColumnSizes) = malloc(sizeof(int)*matSize);
    *returnSize = matSize;
    // Creat distance matrix to be returned
    for (int i = 0; i < matSize; i++){
        ret[i] = malloc(sizeof(int)*matColSize[i]);
        (*returnColumnSizes)[i] = matColSize[i];
    }
    // Initialize distance matrix
    for (int i = 0; i < matSize; i++){
        for (int j = 0; j < matColSize[i]; j++){
            // Initial distance value is 0 where value itself is 0
            if (!mat[i][j]){
                ret[i][j] = 0;
            }
            // Initial distance value inf where value is not zero
            else{
                ret[i][j] = INT_MAX;
            }
        }
    }
    // Traverse the return matrix
    for (int i = 0; i < matSize; i++){
        for (int j = 0; j < matColSize[i]; j++){
            // If distance is 0 normalize distances of nearby cells
            if (!ret[i][j]){
                normalize(ret, matSize, matColSize[i], i, j);
            }
        }
    }
    return ret;
}