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
      
      
      
#       https://leetcode.com/problems/longest-substring-without-repeating-characters/description/
