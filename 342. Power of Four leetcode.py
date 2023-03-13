class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n==1:
            return True
        if n<1:
            return False
        return self.isPowerOfFour(n/4)

# class Solution:
#     def isPowerOfFour(self, n: int) -> bool:
#         if n == 1:
#             return True
#         elif n == 0 or n % 4 != 0:
#             return False
#         else:
#             return self.isPowerOfFour(n//4)


# class Solution:
#     def isPowerOfFour(self, n: int) -> bool:
#         if n==1:
#             return True
#         if n==0 or n%4!=0:
#             return False
#         return self.isPowerOfFour(n//4)



# https://leetcode.com/problems/power-of-four/
