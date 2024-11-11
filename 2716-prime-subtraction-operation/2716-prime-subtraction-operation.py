class Solution:
    def primeSubOperation(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True
        prime = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577, 587, 593, 599, 601, 607, 613, 617, 619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691, 701, 709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787, 797, 809, 811, 821, 823, 827, 829, 839, 853, 857, 859, 863, 877, 881, 883, 887, 907, 911, 919, 929, 937, 941, 947, 953, 967, 971, 977, 983, 991, 997]

        # Returns maximum possible prime number to subtruct if exists else -1
        def isPossible(st: int, curr: int, end: int) -> int:
            nm1, np1 = st, end # nm1(n minus 1) is previous of cuurent and np1 is next of current
            st, end = 0, len(prime) - 1
            ret = -1
            if (nm1 < curr < np1):
                ret = 0
            while st <= end:
                mid = st + (end-st)//2
                if prime[mid] >= curr:
                    end = mid-1
                elif (nm1 < (curr-prime[mid]) < np1):
                    ret = max(ret, prime[mid])
                    st = mid+1
                elif (curr-prime[mid]) <= nm1:
                    end = mid-1
                elif (curr-prime[mid]) >= np1:
                    st = mid+1
            return ret
        
        for i in range(len(nums)):
            if (val:=isPossible((nums[i-1] if i > 0 else -float('inf')), nums[i], (nums[i+1] if i < len(nums)-1 else float('inf')))) == -1:
                return False
            nums[i] -= val
        return True