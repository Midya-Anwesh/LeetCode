class Solution:

    @staticmethod
    def hash(s: str) -> tuple:
        table = [0 for _ in range(26)]
        for ch in s:
            table[ord(ch)-97] += 1
        return tuple(table)

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ret = []
        indices_dict = dict()
        for s in strs:
            if (key := Solution.hash(s)) in indices_dict:
                ret[indices_dict[key]].append(s)
            else:
                indices_dict[key] = len(ret)
                ret.append([s])
        return ret