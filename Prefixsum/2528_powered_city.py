from typing import List
from collections import deque

class Solution:
    def maxPower(self, stations: List[int], r: int, k: int) -> int:
        n = len(stations)
        prefix_sum = []
        curr_s = 0
        for s in stations:
            curr_s += s
            prefix_sum.append(curr_s)
        
        # For each city calculate its initial power
        cities_initial_power = [0 for _ in range(n)]
        for i in range(n):
            left = max(0, i - r)
            right = min(n - 1, i + r)
            power = prefix_sum[right] - (prefix_sum[left - 1] if left > 0 else 0)
            cities_initial_power[i] = power
        
        # bin serach
        range_min = min(cities_initial_power)
        range_max = range_min + k
        res = range_min

        def check_target(target):
            k_left = k
            curr_added_power = 0
            energy_queue = deque()
            for i in range(n):
                while energy_queue:
                    idx, val = energy_queue[0]
                    if idx < i:
                        curr_added_power -= val
                        energy_queue.popleft()
                    else:
                        break

                needed = target - cities_initial_power[i] - curr_added_power
                if needed <= 0:
                    continue
                
                k_left -= needed
                if k_left < 0:
                    return False
                
                curr_added_power += needed
                energy_queue.append((i + 2 * r, needed))

            return True

        while range_min <= range_max:
            mid = (range_min + range_max) // 2
            if check_target(mid):
                res = mid
                range_min = mid + 1
            else:
                range_max = mid - 1
        
        return res
