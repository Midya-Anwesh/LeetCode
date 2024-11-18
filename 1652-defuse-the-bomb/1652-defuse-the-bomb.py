class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        if not k:
            return [0 for _ in range(len(code))]

        ret, win_st, win_end = [], 0, 0

        if k > 0:
            win_st, win_end = 1, k
        else:
            win_st, win_end = ((len(code)+k)%len(code)), len(code)-1

        ret.append(sum(code[win_st:win_end+1]))

        for _ in range(1, len(code)):
            win_end = (win_end+1)%len(code)
            ret.append(ret[-1] - code[win_st] + code[win_end])
            win_st = (win_st+1)%len(code)
        return ret