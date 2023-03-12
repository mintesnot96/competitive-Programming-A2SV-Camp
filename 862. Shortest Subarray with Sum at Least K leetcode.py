class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        result = float('inf')
        psum = [0] * (len(nums) + 1)
        for i in range(len(nums)):
            psum[i + 1] = psum[i] + nums[i]

        dq = collections.deque()
        for right in range(len(nums) + 1):
            while dq and psum[right] - psum[dq[0]] >= k:
                result = min(result, right - dq.popleft())
            while dq and psum[right] <= psum[dq[-1]]:
                dq.pop()
            dq.append(right)

        return result if result != float('inf') else -1
# https://leetcode.com/problems/shortest-subarray-with-sum-at-least-k/description/
