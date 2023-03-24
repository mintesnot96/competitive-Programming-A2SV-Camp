class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        occr=-1
        occl=-1
        left, right=0,len(nums)-1
        while left<=right:
            middle=(left+right)//2
            if target<nums[middle]:
                right=middle-1
            elif target>nums[middle]:
                left=middle+1
            else:
                occr=middle
                left=middle+1
        left, right=0,len(nums)-1
        while left<=right:
            middle=(left+right)//2
            if target<nums[middle]:
                right=middle-1
            elif target>nums[middle]:
                left=middle+1
            else:
                occl=middle
                right=middle-1
        return [occl,occr]
            
            

# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/
