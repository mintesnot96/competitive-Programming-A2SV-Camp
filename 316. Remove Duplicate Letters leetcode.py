
class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        import collections
        counter = collections.Counter(s)
        stack = []
        visited = set()
        for c in s:
            counter[c] -= 1
            if c in visited:
                continue
            while stack and c < stack[-1] and counter[stack[-1]] > 0:
                visited.remove(stack.pop())
            visited.add(c)
            stack.append(c)
        res= ''.join(stack)
        return res
# https://leetcode.com/problems/remove-duplicate-letters/
