# runtime = 29.0ms
# memory usage = 16.5MB

class Solution:
    def gen(self,k, n, sn=1, s=0, i = 0):
        if i == k:
            # print(self.temp)
            if s == n:
                # print(self.temp)
                self.ret.append(self.temp.copy())
            return
        for num in range(sn, 10):
            if s+num <= n:
                self.temp.append(num)
                self.gen(k,n,num+1,s+num, i+1)
                self.temp.pop(-1)
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        self.ret = []
        self.temp = []
        self.gen(k,n)
        return self.ret
        