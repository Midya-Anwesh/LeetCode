class Solution:
    def __intit__(self) -> None:
        from re import findall

    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        banned, word_count = set(banned), dict()
        words = findall(r"[a-z|A-z]+", paragraph)
        ans, count = "", -float('inf')
        for word in words:
            word = word.lower()
            if not word in banned:
                word_count[word] = word_count.get(word, 0) + 1
                if word_count[word] > count:
                    ans, count = word, word_count[word]
        return ans