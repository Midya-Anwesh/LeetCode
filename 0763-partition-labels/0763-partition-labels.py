class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        partition_count = [0]
        last_seen = dict()

        for i in range(len(s)):
            last_seen[s[i]] = max(i, last_seen.get(s[i], 0))

        win_st, win_end = 0, 0

        while win_st < len(s) - 1:
            if win_st > win_end:
                partition_count.append(0)
            partition_count[-1] += 1
            win_end = max(win_end, last_seen[s[win_st]])
            win_st += 1

        if len(s)-1 == win_end:
            partition_count[-1] += 1
        else:
            partition_count.append(1)
            
        return partition_count