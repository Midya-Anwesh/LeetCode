class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2) or set(word1) != set(word2):
            return False
        w1dict, w2dict, count1, count2 = dict(), dict(), dict(), dict()
        for i in range(len(word1)):
            w1dict[word1[i]] = w1dict.get(word1[i], 0) + 1
            w2dict[word2[i]] = w2dict.get(word2[i], 0) + 1
        for letter in w1dict:
            count1[w1dict[letter]] = count1.get(w1dict[letter], 0) + 1
        for letter in w2dict:
            count2[w2dict[letter]] = count2.get(w2dict[letter], 0) + 1
        return count1 == count2