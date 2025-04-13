class Solution:
    def countGoodNumbers(self, n: int) -> int:
        @lru_cache(maxsize=None)
        def fastModulo(base: int, exp: int, mod: int) -> int:
            if exp == 1:
                return base % mod
            elif exp == 0:
                return 1
            if exp & 1:
                return (fastModulo(base, exp-1, mod) * 
                        fastModulo(base, 1, mod)) % mod
            return pow(fastModulo(base, exp // 2, mod), 2) % mod
        mod = 1_000_000_007
        return (fastModulo(5, ceil(n/2), mod) * fastModulo(4, floor(n/2), mod)) % mod