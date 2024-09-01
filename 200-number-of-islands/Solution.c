// runtime = 15.0ms
// memory usage = 8.6MB

void mark_visited(char** grid, int i, int j, int r, int c){
    //printf("%d,%d\n",i,j);
    grid[i][j] = NULL;

    if(i < r-1 && grid[i+1][j]=='1'){

        mark_visited(grid,i+1,j,r,c);

    }
    if(i > 0 && grid[i-1][j]=='1'){
        mark_visited(grid,i-1,j,r,c);
    }

    if(j < c-1&&grid[i][j+1]=='1'){

        mark_visited(grid,i,j+1,r,c);

    }
    if(j >= 1 && grid[i][j-1]=='1'){
        mark_visited(grid,i,j-1,r,c);
    }

}

int numIslands(char** grid, int gridSize, int* gridColSize) {
    int ret = 0;
    for(int i = 0; i < gridSize; i++){
        for(int j = 0; j < *gridColSize; j++){
            if(grid[i][j]=='1'){
                ret += 1;
                mark_visited(grid,i,j,gridSize,*gridColSize);
            }
        }
        }
    return ret;
}