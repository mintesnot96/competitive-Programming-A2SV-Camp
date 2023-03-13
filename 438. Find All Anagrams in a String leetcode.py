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
  
  
# other method
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        result = []
        # s = "cbaebabacd", p = "abc"
        tarWin=collections.Counter(p)
        currentWin=collections.Counter(s[:len(p)-1])
        for i in range(len(p)-1,len(s)):
            currentWin[s[i]]+=1
            if tarWin==currentWin:
                result.append(i-len(p)+1)
                # currentWin[s[i-len(p)+1]]-=1
            currentWin[s[i-len(p)+1]]-=1
            if currentWin[s[i-len(p)+1]]==0:
                del currentWin[s[i-len(p)+1]]
        return result
  
#   https://leetcode.com/problems/longest-substring-without-repeating-characters/
