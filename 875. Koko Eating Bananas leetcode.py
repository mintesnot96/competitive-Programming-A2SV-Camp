# https://leetcode.com/problems/koko-eating-bananas/
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # [3,6,7,11], h = 8 k eating speed
        # 1...4..8..11
        left = 1
        right = max(piles)
        result = right 
        while left <= right:
            k = (left + right) // 2
            hours = 0
            for pile in piles:
                hours += (pile - 1) // k + 1 
            if hours <= h:
                result = min(result, k)
                right = k - 1
            else:
                left = k + 1          
        return result
        
