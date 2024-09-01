# runtime = 69.0ms
# memory usage = 16.5MB

class Solution:
    def count_possibility(self, tiles: dict(), length: int, temp: list[str] = []):
        # print(temp)
        if len(temp) and len(temp) <= length:
            # print("".join(temp))
            self.count += 1
           

        for letter in tiles:
            if tiles[letter]:
                tiles[letter] -= 1
                temp.append(letter)
                self.count_possibility(tiles, length, temp)
                temp.pop(-1)
                tiles[letter] += 1

    def numTilePossibilities(self, tiles: str) -> int:
        tiles_dict, self.count = dict(), 0
        for letter in tiles:
            tiles_dict[letter] = tiles_dict.get(letter, 0) + 1

        self.count_possibility(tiles_dict, len(tiles))
        return self.count