class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:

        Maxsum=0
        for l in range(k):
            Maxsum=Maxsum+nums[l]
        sum1=Maxsum
        for i in range(k,len(nums)):
            sum1=sum1+nums[i]-nums[i-k]
            Maxsum=max(Maxsum,sum1)             
        return Maxsum/k
   
   
   
   # https://leetcode.com/problems/maximum-average-subarray-i/description/ 
