from collections import defaultdict
class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        charFreq = [0 for _ in range(26)]
        prefix = [[0 for _ in range(26)]]
        idxMap = defaultdict(lambda:[float('inf'), -float('inf')])
        for idx, char in enumerate(s):
            idxMap[char][0] = min(idxMap[char][0], idx)
            idxMap[char][1] = max(idxMap[char][1], idx)
            prefix.append(prefix[-1].copy())
            prefix[-1][ord(char)-97] += 1

        pallindromes = 0
        charsSeen = set()
        for char in s:
            if char in charsSeen:
                continue
            charsSeen.add(char)
            leftIdx, rightIdx = idxMap[char]
            currSet = [prefix[rightIdx][i] - prefix[leftIdx][i] for i in range(26)]
            currSet[ord(char)-97] -= 1
            pallindromes += sum(freq >= 1 for freq in currSet)
        return pallindromes