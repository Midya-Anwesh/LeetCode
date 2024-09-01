# runtime = 56.0ms
# memory usage = 16.3MB

class Solution:
    def gen_combi(self, target: int, s: int, unique_combinations: dict[tuple[int]], combi: list[int] = []):
        if s == target:
            unique_combinations.update({tuple(sorted(combi)): 0})
        if s < target:
            for num in self.num_map:
                if self.num_map[num] and s + num <= target :
                    combi.append(num)
                    self.num_map[num] -= 1
                    self.gen_combi(target, s+num, unique_combinations, combi)
                    combi.pop(-1)
                    self.num_map[num] += 1
            
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        unique_combinations, self.num_map = dict(), dict()
        for num in candidates:
            self.num_map[num] = self.num_map.get(num, 0) + 1
        self.gen_combi(target, 0, unique_combinations)
        return unique_combinations.keys()
        