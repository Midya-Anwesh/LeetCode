// runtime = 387.0ms
// memory usage = 59.8MB

/**
 * Return an array of arrays of size *returnSize.
 * The sizes of the arrays are returned as *returnColumnSizes array.
 * Note: Both returned array and *columnSizes array must be malloced, assume caller calls free().
 */
int** construct2DArray(int* original, int originalSize, int m, int n, int* returnSize, int** returnColumnSizes) {
    if (originalSize != m*n){
        *returnSize = 0;
        *returnColumnSizes = NULL;
        return NULL;
    }
    int **matrix = (int **)calloc(sizeof(int *), m), *columnSizes = (int *)calloc(sizeof(int), m);
    *returnSize = m;

    for (int k = 0, i = 0, j = 0; k < originalSize; k++, i += !(k%n), j = k%n){
        if (!matrix[i]){
            matrix[i] = (int *)calloc(sizeof(int), n);
            columnSizes[i] = n;
        }
        matrix[i][j] = original[k];
    }
    *returnColumnSizes = columnSizes;
    return matrix;
}