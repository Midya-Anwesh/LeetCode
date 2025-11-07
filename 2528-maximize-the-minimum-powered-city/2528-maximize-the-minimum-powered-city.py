from typing import List

class Solution:
    def maxPower(self, stations: List[int], r: int, k: int) -> int:
        n = len(stations)

        # Base power each city receives from existing stations
        prefix = [0]
        for s in stations:
            prefix.append(prefix[-1] + s)
        base_power = [0] * n
        for i in range(n):
            l = max(0, i - r)
            rgt = min(n - 1, i + r)
            base_power[i] = prefix[rgt + 1] - prefix[l]

        # Feasibility check (adds allowed only to current or previous stations)
        def isPossible(minPower: int) -> bool:
            added_diff = [0] * (n + 1)
            window_added_power = 0
            kRem = k

            for i in range(n):
                window_added_power += added_diff[i]
                total = base_power[i] + window_added_power

                if total < minPower:
                    need = minPower - total
                    if need > kRem:
                        return False
                    kRem -= need

                    # Add 'need' power at station i (can affect next r cities)
                    window_added_power += need
                    end = i + 2 * r + 1  # stops affecting after i + r
                    if end < len(added_diff):
                        added_diff[end] -= need

            return True

        # Binary search over the answer
        low, high = min(base_power), sum(stations) + k
        ans = low
        while low <= high:
            mid = (low + high) // 2
            if isPossible(mid):
                ans = mid
                low = mid + 1
            else:
                high = mid - 1
        return ans
