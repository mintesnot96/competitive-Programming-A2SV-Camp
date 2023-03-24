# https://leetcode.com/problems/sqrtx/
class Solution:
    def mySqrt(self, x: int) -> int:
        left=1
        right=x
        ans=0
        # 1 2 3 4 5 6 7 8 mid 4
        while left<=right:
            mid=(left+right)//2
            if mid*mid==x:
                return mid
            if mid*mid<x:
                left=mid+1
                ans=mid
            else:
                right=mid-1
        return ans
