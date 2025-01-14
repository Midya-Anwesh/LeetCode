class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        # Convert A to hash map, where number maps to its index
        A = {num:i for i, num in enumerate(A)}
        # Return vector
        ret = [0]*len(A)
        # Traverse the B array
        for i, num in enumerate(B):
            # Update the return vector, at which index both array will have num
            ret[max(i, A[num])] += 1
        # Do a prefix sum
        for i in range(1, len(ret)):
            ret[i] = ret[i-1]+ret[i]
        # Return the vector
        return ret