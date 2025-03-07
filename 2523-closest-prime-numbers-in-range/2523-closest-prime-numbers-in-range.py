class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        prime = [True]*(right+1)

        for num in range(2, right+1):
            if prime[num]:
                for i in range(num*num, right+1, num):
                    prime[i] = False
        
        prime = [i for i in range(len(prime)) if prime[i] and i >= max(left,2) and i <= right]
        if len(prime) < 2:
            return [-1, -1]
        
        ret, diff = [-1, -1], float('inf')
        for i in range(len(prime)-1):
            if diff > prime[i+1] - prime[i]:
                diff = prime[i+1] - prime[i]
                ret = [prime[i], prime[i+1]]
        
        return ret