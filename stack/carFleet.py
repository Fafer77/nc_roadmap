from typing import List

"""
Notice that we can sort cars descending based on their distance to target. Why?
Because if there is faster car it won't reach target before car in front of it, but
will sit on its back.
We consider how much time each car need to reach target (do not care whether there is car ahead).
Then we push values on a stack if time of considered car is higher than the one of the top.
If considered car time to target is lower or equal it means that they will create car fleet.
Answer is len of stack
"""

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pos_speed = list(zip(position, speed))
        pos_speed.sort(key=lambda ps: ps[0], reverse=True)
        
        time_to_target = [((target - ps[0]) / ps[1]) for ps in pos_speed]
        stack = [time_to_target[0]]
        car_fleets = 1

        for i in range(1, len(position)):
            if time_to_target[i] > stack[-1]:
                car_fleets += 1
                stack.append(time_to_target[i])

        return car_fleets


sol = Solution()
print(sol.carFleet(target = 10, position = [1,4], speed = [3,2]))
