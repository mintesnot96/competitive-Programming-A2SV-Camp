class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l=0
        r=len(s1)-1
        target_counts = collections.Counter(s1)
        if len(s1)>len(s2):
            return False
        while l<len(s2):
            cwindow=collections.Counter(s2[l:r+1])
            if target_counts==cwindow:
                return True
            l+=1
            r+=1
        return False
 

# https://leetcode.com/problems/permutation-in-string/description/
