# runtime = 2374.0ms
# memory usage = 16.5MB

class Solution:

    def is_beautiful(self, s: str):

        return all(s.count(num) == int(num) for num in set(s))

        

    def nextBeautifulNumber(self, n: int) -> int:

        n += 1

        while(not self.is_beautiful(str(n))):

            n += 1

        return n

        