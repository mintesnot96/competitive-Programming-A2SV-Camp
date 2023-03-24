# https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/
class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        # weights = [1,2,3,4,5,6,7,8,9,10], days = 5
        low=max(weights)
        high=sum(weights)
        while low<high:
            mid=(low+high)//2
            day=1
            wsum=0
            for w in weights:
                wsum=w+wsum
                if wsum>mid:
                    day+=1
                    wsum=w
            if day>days:
                low=mid+1
            else:
                high=mid
        return low


    

