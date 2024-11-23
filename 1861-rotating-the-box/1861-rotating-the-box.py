class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        ret = [['.' for _ in range(len(box))] for _ in range(len(box[0]))]
        ret_col = 0
        for row in range(len(box)-1, -1, -1):
            ret_row = len(box[0])-1
            for col in range(len(box[0])-1, -1, -1):
                if box[row][col] == '#':
                    curr = ret_row
                    while (curr < len(box[0])) and (ret[curr][ret_col]== '.'):
                        curr += 1
                    ret[curr-1][ret_col] = '#'
                else:
                    ret[ret_row][ret_col] = box[row][col]
                ret_row -= 1
            ret_col += 1
        return ret
                