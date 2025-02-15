from re import fullmatch
class Solution:
    def valid(self, s: str, target: int, index: int, prev: int):
        if index >= len(s):
            if prev == target:
                return True
            return False

        for i in range(index + 1, len(s)+1):
            sa = s[index : i]
            if re.fullmatch(r"(?:0|(?:[1-9]+[0-9]*))", sa) and (curr := int(sa) + prev) <= target:
                if self.valid(s, target, i, curr):
                    return True
            elif fullmatch(r"0[0-9]+", sa):
                return False
        return False

    def punishmentNumber(self, n: int) -> int:
        return sum(num * num for num in filter(lambda i:((i*i)%9 <= 1) and self.valid(str(i*i), i, 0, 0), range(1, n+1)))