# runtime = 396.0ms
# memory usage = 46.7MB

from functools import lru_cache
class Solution:
    @lru_cache(maxsize=None)
    def w_diff(self, w1: str, w2: str):
        return sum(int(w[0]!=w[1]) for w in zip(w1, w2))
    
    def gen(self, words: set[str], s: str, e: str):
        q, step = [s], [{s}]
        while len(q) and not self.found:
            next_level = set()
            for w1 in q:
                next_level = next_level.union(set(filter(lambda w2: self.w_diff(w1, w2) == 1, words)))
                words -= next_level
            words = words - set(q)
            q = next_level
            step.append(q)
            if e in q:
                self.found = True
                break
        if not self.found:
            return None
        step[-1] = {e}
        for i in range(len(step)-2, 0, -1):
            temp = set()
            for w1 in step[i+1]:
                temp = temp.union(set(filter(lambda w2: self.w_diff(w1, w2) == 1, step[i])))
            step[i] = temp
        return step


    def print_path(self, index: int = 0, temp: list[str] = []):
        if len(temp) >= len(self.path_builder):
            yield temp
            return
        for w in self.path_builder[index]: 
            if self.w_diff(w, temp[-1]) == 1:
                temp.append(w)
                yield from self.print_path(index+1, temp)
                temp.pop(-1)


    def findLadders(self, beginWord: str, endWord: str, wordList: list[str]) -> list[list[str]]:
        self.found = False
        wordList = set(wordList)
        wordList.add(beginWord)
        if not endWord in wordList:
            return []

        self.path_builder = self.gen(wordList , beginWord, endWord)
        yield from self.print_path(1, [beginWord]) if self.found else []