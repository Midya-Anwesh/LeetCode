# runtime = 142.0ms
# memory usage = 19.1MB

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        unplantable = []
        for i in range(len(flowerbed)):
            if flowerbed[i]:
                unplantable.extend([i-1, i, i+1])
        plnt = list(set(range(len(flowerbed))) - set(unplantable))
        if not len(plnt):
            return len(plnt) >= n
        plnt.sort()
        p = [plnt[0]]
        for ele in plnt:
            if p[-1] < ele - 1:
                p.append(ele)
        #print(p)
        return len(p) >= n