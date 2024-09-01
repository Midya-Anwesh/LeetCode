# runtime = 456.0ms
# memory usage = 31.4MB

class Solution:
    def p(self, s, i, j):
        while(i < j):
            

            if s[i] != s[j]:
                return False
	        
            i += 1
            j -= 1


        return True


    def gen(self, s, si = 0):
        if si >= len(s):
            self.ret.append(self.temp.copy())
            return
        for i in range(si, len(s)):

            if self.p(s, si, i):
                self.temp.append(s[si:i+1])
                self.gen(s, i+1)
                self.temp.pop(-1)

    def partition(self, s: str) -> List[List[str]]:
        self.temp = []
        self.ret = []
        self.gen(s)
        return self.ret

        