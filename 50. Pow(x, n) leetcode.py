class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n==0:
            return 1.0
        if n<0:
            return 1/self.myPow(x,-1*n)
        elif n%2==0:
            return self.myPow(x*x,n//2)
        return x*self.myPow(x,n-1)


            
         

# https://leetcode.com/problems/powx-n/description/
