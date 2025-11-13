class Solution:
    def maxOperations(self, s: str) -> int:
        maxOps = 0
        idx = 0
        consicutiveOnes = 0
        while idx < len(s):
            # Go to index where '1' is present
            while idx < len(s) and s[idx] != '1':
                idx += 1
            # Now count how many consicutive '1's are there
            while idx < len(s) and s[idx] == '1':
                consicutiveOnes += 1
                idx += 1
            # Count how many '0's are there before the end of the string from now on till the end
            if idx < len(s) and s[idx] == '0':
                maxOps += consicutiveOnes
                while idx < len(s) and s[idx] == '0':
                    idx += 1
        return maxOps