class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        pattern_count = {}
        for char in p:
            pattern_count[char] = pattern_count.get(char, 0) + 1
        result = []
        window_count = {}
        for i in range(len(s)):
            if s[i] not in window_count:
                window_count[s[i]] = 0
            window_count[s[i]] += 1
            if i >= len(p):
                if window_count[s[i - len(p)]] == 1:
                    del window_count[s[i - len(p)]]
                else:
                    window_count[s[i - len(p)]] -= 1
            if i >= len(p) - 1 and window_count == pattern_count:
                result.append(i - len(p) + 1)
        return result
  
  
  
#   https://leetcode.com/problems/longest-substring-without-repeating-characters/
