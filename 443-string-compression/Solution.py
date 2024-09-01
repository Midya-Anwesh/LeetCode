# runtime = 47.0ms
# memory usage = 16.8MB

class Solution:
    def compress(self, chars: List[str]) -> int:
        ret,i = [],0
        from itertools import groupby
        for k,g in groupby(chars):
            l = len(list(g))
            i += 1
            ret.append(k)
            if l > 1:
                for c in str(l):
                    ret.append(c)
                    i += 1
        #print(ret)
        chars[:]=ret
        return i