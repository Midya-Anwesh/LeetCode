class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        sarr = sorted(arr)
        win_elements = dict()
        partition_count = 0
        for i in range(len(arr)):
            win_elements[arr[i]] = win_elements.get(arr[i],   0) + 1
            win_elements[sarr[i]] = win_elements.get(sarr[i], 0) - 1

            if not win_elements[arr[i]]: # If we get same element in this index
                win_elements.pop(arr[i])

            if not win_elements.get(sarr[i], True): # If a previous element is seen also handle edge, when both elements are same
                win_elements.pop(sarr[i])

            if not len(win_elements): # If dict is empty then we got a suitable window
                partition_count += 1
                
        return partition_count