class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        groups = defaultdict(list)
        ret = []
        for idx, num in enumerate(groupSizes):
            groups[num].append(idx)
            if len(groups[num]) == num:
                ret.append(groups[num])
                groups[num] = []
        return ret