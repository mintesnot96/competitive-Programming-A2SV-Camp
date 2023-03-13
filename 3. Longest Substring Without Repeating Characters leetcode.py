class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxim=0
        lstring=set()
        left=0
        for i in range(len(s)):
            while s[i] in lstring:
                lstring.remove(s[left])
                left+=1
            lstring.add(s[i])
            maxim=max(maxim,len(lstring))
        return maxim
      
# or


# class Solution:
#     def lengthOfLongestSubstring(self, s: str) -> int:
#         maxim = 0
#         substr_dict = {}
#         left = 0
#         for i in range(len(s)):
#             if s[i] in substr_dict and substr_dict[s[i]] >= left:
#                 left = substr_dict[s[i]] + 1
#             substr_dict[s[i]] = i
#             maxim = max(maxim, i - left + 1)
#         return maxim
      
      
#       https://leetcode.com/problems/longest-substring-without-repeating-characters/description/
