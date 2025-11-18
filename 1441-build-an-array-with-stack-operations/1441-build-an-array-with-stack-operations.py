class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        idx, ops = 0, []
        for num in range(1, n+1):
            if idx >= len(target):
                break
            ops.append("Push")
            if num == target[idx]:
                idx += 1
            else:
                ops.append("Pop")
        return ops if idx >= len(target) else []