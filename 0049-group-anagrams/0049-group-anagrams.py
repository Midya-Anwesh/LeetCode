class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ret = []
        indices_dict = dict()
        for s in strs:
            if (key := tuple(sorted(s))) in indices_dict:
                ret[indices_dict[key]].append(s)
            else:
                indices_dict[key] = len(ret)
                ret.append([s])
        return ret