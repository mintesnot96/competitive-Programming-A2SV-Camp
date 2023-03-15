# class Solution:
#     def PredictTheWinner(self, nums: List[int]) -> bool:
#         memo = {}

#         def can_win(l, r):
#             if l == r:
#                 return nums[l]

#             if (l, r) in memo:
#                 return memo[(l, r)]

#             x = nums[l] - can_win(l + 1, r)
#             y = nums[r] - can_win(l, r - 1)
#             memo[(l, r)] = max(x, y)
#             return memo[(l, r)]

#         return can_win(0, len(nums) - 1) >= 0

class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        def canp1win(l, r, p1):
            if l == r:
                return nums[l] if p1 else -nums[l]
            if p1:
                x = nums[l] + canp1win(l + 1, r, False)
                y = nums[r] + canp1win(l, r - 1, False)
                return max(x, y)
            else:
                x = -nums[l] + canp1win(l + 1, r, True)
                y = -nums[r] + canp1win(l, r - 1, True)
                return min(x, y)
        return canp1win(0, len(nums) - 1, True) >= 0



# https://leetcode.com/problems/predict-the-winner/description/
