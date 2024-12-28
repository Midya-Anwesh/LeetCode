class Solution:
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        # Variables to track the best indices for one, two, and three subarray configurations
        best_single_index, best_double_index, best_triple_index = 0, [0, k], [0, k, 2*k]

        # Compute the initial sums for the first three subarrays
        single_sum = sum(nums[:k])
        double_sum = sum(nums[k : 2*k])
        triple_sum = sum(nums[2*k : 3*k])

        # Track the best sums found so far
        best_single_sum = single_sum
        best_double_sum = single_sum + double_sum
        best_triple_sum = single_sum + double_sum + triple_sum

        # Sliding window pointers for the subarrays
        single_start = 1
        double_start = k + 1
        triple_start = 2*k + 1

        # Slide the windows across the array
        while triple_start <= len(nums)-k:
            # Update the sums using the sliding window technique
            single_sum = single_sum - nums[single_start - 1] + nums[single_start + k - 1]
            double_sum = double_sum - nums[double_start - 1] + nums[double_start + k - 1]
            triple_sum = triple_sum - nums[triple_start - 1] + nums[triple_start + k - 1]

            # Update the best single subarray start index if a better sum is found
            if single_sum > best_single_sum:
                best_single_index = single_start
                best_single_sum = single_sum
            
            # Update the best double subarray start indices if a better sum is found
            if best_single_sum + double_sum > best_double_sum:
                best_double_index[0] = best_single_index
                best_double_index[1] = double_start
                best_double_sum = best_single_sum + double_sum

            # Update the best triple subarray start indices if a better sum is found
            if best_double_sum + triple_sum > best_triple_sum:
                best_triple_index[0] = best_double_index[0]
                best_triple_index[1] = best_double_index[1]
                best_triple_index[2] = triple_start
                best_triple_sum = best_double_sum + triple_sum

            # Move the sliding windows forward
            single_start += 1
            double_start += 1
            triple_start += 1

        # Return the starting indices of the three subarrays with the maximum sum
        return best_triple_index