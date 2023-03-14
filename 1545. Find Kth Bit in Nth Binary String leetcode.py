class Solution(object):
    def reverse(self, s):
        return s[::-1]
    
    def invert(self, s):
        return ''.join(['0' if c == '1' else '1' for c in s])
    
    def findKthBit(self, n, k):
        def find_helper(n):
            if n == 1:
                return '0'
            return find_helper(n - 1) + '1' + self.reverse(self.invert(find_helper(n - 1)))
        
        s = find_helper(n)
        return s[k - 1]
   

#  https://leetcode.com/problems/find-kth-bit-in-nth-binary-string/
