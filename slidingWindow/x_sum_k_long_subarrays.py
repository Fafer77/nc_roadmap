from sortedcontainers import SortedList
from collections import Counter
from typing import List

'''
Gameplan:
Needed:
-> Counter - to store frequencies of particular numbers in each window
-> SortedList top_x - to store x elements which occur the most amount of times. Keep them sorted
-> SortedList other - to store other elements which are not in top x frequencies

1. For each window update frequencies
2. Remove tuples for old and new and add them with updated frequencies to other
3. Balance as long as len(top_x) < x by adding from other
4. Balance if there is better element in other by swapping with last element from top_x
In steps 2-4 update x_sum accordingly
'''

class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        freq_map = Counter(nums[:k])
        
        all_tuples = SortedList()
        for val, freq in freq_map.items():
            if freq > 0:
                all_tuples.add((-freq, -val))

        top_x = SortedList(all_tuples[:x])
        other = SortedList(all_tuples[x:])

        x_sum = 0
        for freq_tuple, val_tuple in top_x:
            val = -val_tuple
            freq = -freq_tuple
            x_sum += (val * freq)
        
        res = [x_sum]
        
        for i in range(k, len(nums)):
            new = nums[i]
            old = nums[i - k]

            if new == old:
                res.append(x_sum)
                continue
            
            old_freq = freq_map[old]
            if old_freq > 0:
                old_tuple = (-old_freq, -old)
                
                if old_tuple in top_x:
                    top_x.remove(old_tuple)
                    x_sum -= (old * old_freq)
                else:
                    other.remove(old_tuple)
            
            new_freq = freq_map.get(new, 0)
            if new_freq > 0:
                new_tuple = (-new_freq, -new)
                if new_tuple in top_x:
                    top_x.remove(new_tuple)
                    x_sum -= (new * new_freq)
                else:
                    other.remove(new_tuple)

            freq_map[old] -= 1
            freq_map[new] += 1

            if freq_map[old] > 0:
                other.add((-freq_map[old], -old))
            
            if freq_map[new] > 0:
                other.add((-freq_map[new], -new))

            while len(top_x) < x and other:
                b = other.pop(0)
                b_val = -b[1]
                b_freq = -b[0]
                top_x.add(b)
                x_sum += (b_val * b_freq)

            while top_x and other and top_x[-1] > other[0]:
                a = top_x.pop(-1)
                a_val = -a[1]
                a_freq = -a[0]
                
                b = other.pop(0)
                b_val = -b[1]
                b_freq = -b[0]
                
                top_x.add(b)
                other.add(a)
                
                x_sum -= (a_val * a_freq)
                x_sum += (b_val * b_freq)
            
            res.append(x_sum)
        
        return res