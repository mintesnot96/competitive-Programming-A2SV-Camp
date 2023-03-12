class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        t = {}
        for i in range(len(position)):
            t[position[i]] = (target - position[i]) / speed[i]
        cars = sorted(t.items(), key=lambda x: x[0], reverse=True)

        fleet_count = 0
        max_time = 0
        for pos, time in cars:
            if time > max_time:
                fleet_count += 1
                max_time = time

        return fleet_count


# https://leetcode.com/problems/car-fleet/description/
