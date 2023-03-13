class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = r = 0
        c = {}
        mx_len = 0
        mx_cnt = 0
        while r < len(s):
            c[s[r]] = c.get(s[r], 0) + 1
            mx_cnt = max(mx_cnt, c[s[r]])
            if r - l + 1 - mx_cnt > k:
                c[s[l]] -= 1
                l += 1
            mx_len = max(mx_len, r - l + 1)
            r += 1
        return mx_len




# https://leetcode.com/problems/longest-repeating-character-replacement/
