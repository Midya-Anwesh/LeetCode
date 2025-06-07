class Solution:
    def maxCandies(self, status: List[int], candies: List[int], keys: List[List[int]], containedBoxes: List[List[int]], initialBoxes: List[int]) -> int:
        def bfs() -> int:
            OpenBoxes = []
            currCandies = 0
            prevOpend = set()
            lockedBoxes = set()
            for box in initialBoxes:
                if status[box]: # 1 means open
                    OpenBoxes.append(box)
                    prevOpend.add(box)
                else:
                    lockedBoxes.add(box)
            while len(OpenBoxes):
                currBox = OpenBoxes.pop(-1)
                currCandies += candies[currBox]
                for box in containedBoxes[currBox]:
                    if (status[box]) and (box not in prevOpend):
                        OpenBoxes.append(box)
                        prevOpend.add(box)
                    elif (not status[box]):
                        lockedBoxes.add(box)
                for key in keys[currBox]:
                    if (key not in prevOpend) and (key in lockedBoxes):
                        lockedBoxes.discard(key)
                        status[key] = 1
                        OpenBoxes.append(key)
                        prevOpend.add(key)
            return currCandies
        return bfs()