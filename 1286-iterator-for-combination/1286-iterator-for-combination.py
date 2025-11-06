class CombinationIterator:

    def __init__(self, characters: str, combinationLength: int):
        self.queue, self.lst, self.len, self.temp = [], sorted(characters), combinationLength, []
        self.gen_combi()

    def next(self, index: int = 0) -> str:
        if len(self.queue):
            return self.queue.pop(0)

    def hasNext(self) -> bool:
        return bool(len(self.queue))

    def gen_combi(self, index: int = 0):
        if len(self.temp) == self.len:
            self.queue.append("".join(self.temp))
            return

        for i in range(index, len(self.lst)):
            self.temp.append(self.lst[i])
            self.gen_combi(i+1)
            self.temp.pop(-1)
        


# Your CombinationIterator object will be instantiated and called as such:
# obj = CombinationIterator(characters, combinationLength)
# param_1 = obj.next()
# param_2 = obj.hasNext()