# runtime = 58.0ms
# memory usage = 16.4MB

import re
class Solution:
    def insert_dot(self, s: list[str]):
        dotted_s = "".join(s)
        if re.fullmatch(r"(?:(?:[1-9][0-9]*)|0)", dotted_s):
            yield dotted_s

        for i in range(1, len(s)):
            s.insert(i, ".")
            dotted_s = "".join(s)
            if re.fullmatch(r"(?:(?:[1-9][0-9]*)|0)\.(?:[0-9]*[1-9])", dotted_s):
                yield dotted_s
            s.pop(i)


    def insert_comma(self, s: list[str]):
        for i in range(1, len(s)):
            l_str, r_str = s[:i], s[i:]
            for valid_left_str in self.insert_dot(l_str):
                for valid_right_str in self.insert_dot(r_str):
                    yield f"({valid_left_str}, {valid_right_str})"

    def ambiguousCoordinates(self, s: str) -> List[str]:
        yield from self.insert_comma(list(s[1:-1]))