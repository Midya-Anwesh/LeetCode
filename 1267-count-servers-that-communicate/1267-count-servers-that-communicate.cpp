class Solution {
public:
    int countServers(vector<vector<int>>& grid) {
        int gridSize = grid.size();
        int col = grid[0].size();
        int *gridColSize = &col;
        int **seen = (int**)calloc(sizeof(int*), gridSize);
    for (int i = 0; i < gridSize; i++){
        seen[i] = (int*)calloc(sizeof(int), (*gridColSize));
    }
    int connected = 0;

    for (int i = 0; i < gridSize; i++){
        int frow = 0, fcol = 0, comAll = 0, comSeen = 0;
        for (int j = 0; j < (*gridColSize); j++){
            if (grid[i][j]){
                if (!comAll){
                    frow = i; fcol = j;
                }
                comAll += 1;
                comSeen += ((seen[i][j] >= 1)? 1:0);
                seen[i][j] += 1;
            }
        }
        if (comAll == 1){
            seen[frow][fcol] -= 1;
        }
        else if (comAll > 1){
            connected += comAll-comSeen;
        }
    }

    for (int j = 0; j < (*gridColSize); j++){
        int frow = 0, fcol = 0, comAll = 0, comSeen = 0;
        for (int i = 0; i < gridSize; i++){
            if (grid[i][j]){
                if (!comAll){
                    frow = i; fcol = j;
                }
                comAll += 1;
                comSeen += ((seen[i][j] >= 1) ? 1:0);
                seen[i][j] += 1;
            }
        }
        if (comAll == 1){
            seen[frow][fcol] -= 1;
        }
        else if (comAll > 1){
            connected += comAll-comSeen;
        }
    }

    return connected;
    }
};