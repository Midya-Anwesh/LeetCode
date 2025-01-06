class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        boxes = list(map(int, boxes))
        temp = boxes.copy()

        prefixImportCost, suffixImportCost = [0]*len(boxes), [0]*len(boxes)

        for i in range(1, len(boxes)):
            prefixImportCost[i] = prefixImportCost[i-1] + boxes[i-1]
            boxes[i] += boxes[i-1]

            suffixImportCost[len(boxes)-i-1] = suffixImportCost[len(boxes)-i] + temp[len(boxes)-i]
            temp[len(boxes)-i-1] += temp[len(boxes)-i]
        
        return [prefixImportCost[i] + suffixImportCost[i] for i in range(len(boxes))]