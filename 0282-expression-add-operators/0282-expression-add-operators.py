class Solution:
    def addOperators(self, nums: str, target: int) -> List[str]:
        if len(nums) == 1:
            return []

        def dfs(idx: int, temp: List[int]) -> Generator | None:
            if idx >= len(nums):
                yield temp
                return

            if nums[idx] == "0":
                temp.append("0")
                yield from dfs(idx+1, temp)
                temp.pop()
            else:
                for i in range(idx, len(nums)):
                    temp.append(nums[idx:i+1])
                    yield from dfs(i+1, temp)
                    temp.pop()

        def pathToTarget(idx: int, temp: str) -> None:
            nonlocal ans
            if idx >= len(numbers):
                if eval(temp) == target:
                    ans.append(temp[:])
                return 
            
            for op in ("+", "-", "*"):
                pathToTarget(idx+1, temp+op+numbers[idx])
        
        numbers = []
        ans = []
        for comb in dfs(0, []):
            numbers = comb.copy()
            pathToTarget(1, numbers[0])
        return ans