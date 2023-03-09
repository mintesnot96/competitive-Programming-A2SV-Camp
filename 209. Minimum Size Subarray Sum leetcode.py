class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        minl=float('inf')
        left=0
        right=1
        window_sum = 0
        for right in range(len(nums)):
            window_sum += nums[right]
            while window_sum>=target:
                minl=min(minl,right-left+1)
                window_sum -= nums[left]
                left+=1
        return minl if minl != float('inf') else 0
# https://leetcode.com/problems/minimum-size-subarray-sum/description/
