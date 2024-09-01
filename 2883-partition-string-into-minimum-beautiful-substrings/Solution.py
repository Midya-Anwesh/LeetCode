# runtime = 47.0ms
# memory usage = 16.5MB

class Solution:
    def partition(self, s: str, index: int = 0, partition_count: int = -1):
        if index >= len(s):
            self.solved = True
            self.minimum_partition = partition_count+1
            return
        
        if s[index] == "0":
            return

        for i in range(len(s), index-1, -1):
            if s[index : i] in self.patterns:
                self.partition(s, i, partition_count+1)
                if self.solved:
                    return

    def minimumBeautifulSubstrings(self, s: str) -> int:
        self.patterns = {bin(5**i)[2:] for i in range(7)}
        self.minimum_partition, self.solved = -1, False
        self.partition(s, 0, -1)
        return self.minimum_partition