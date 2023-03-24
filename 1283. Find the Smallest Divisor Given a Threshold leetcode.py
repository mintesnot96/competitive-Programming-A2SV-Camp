class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:    
        
        # [1,2,5,9], threshold = 6
        left=1
        right=max(nums)
        def c(g):
            ans=0
            for n in nums:
                ans+=math.ceil(n/g)
            return ans<=threshold
        answe=right
        while left<=right:
            middle=(left+right)//2
            if c(middle):
                right=middle-1
                answe=middle 
            else:
                left=middle+1
        return answe




# https://leetcode.com/problems/find-the-smallest-divisor-given-a-threshold/description/
