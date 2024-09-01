# runtime = 428.0ms
# memory usage = 17.2MB

class Solution:
    def gen(self, s: list[str], index: int = 0):
        if index >= len(self.indices):
            key = "".join(s)
            if not key in self.memo:
                self.memo.add(key)
                yield key
            return
        for i in range(index, len(self.indices)):
            s[self.indices[i]] = s[self.indices[i]].lower()
            yield from self.gen(s, i+1)
            s[self.indices[i]] = s[self.indices[i]].upper()
            yield from self.gen(s, i+1)

    def letterCasePermutation(self, s: str) -> list[str]:
        self.indices = [i for i in range(len(s)) if s[i].isalpha()]
        self.memo = set()
        yield from self.gen(list(s))
