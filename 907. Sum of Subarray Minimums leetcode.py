
class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:        
        MOD = 10**9 + 7
        n = len(arr)
        left = [0] * n
        right = [0] * n
        stack = []
        for i in range(n):
            while stack and arr[stack[-1]] > arr[i]:
                stack.pop()
            left[i] = stack[-1] + 1 if stack else 0
            stack.append(i)
        stack = []
        for i in range(n-1, -1, -1):
            while stack and arr[stack[-1]] >= arr[i]:
                stack.pop()
            right[i] = stack[-1] - 1 if stack else n-1
            stack.append(i)
        ans = 0
        for i in range(n):
            ans += (i - left[i] + 1) * (right[i] - i + 1) * arr[i]
            ans %= MOD
        return ans


# https://leetcode.com/problems/sum-of-subarray-minimums/description/
