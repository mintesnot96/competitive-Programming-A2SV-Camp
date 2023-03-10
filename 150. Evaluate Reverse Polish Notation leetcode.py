class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        s = []
        for t in tokens:
            if t in ['+', '-', '*', '/']:
                b = s.pop()
                a = s.pop()
                if t == '+':
                    res = a + b
                elif t == '-':
                    res = a - b
                elif t == '*':
                    res = a * b
                elif t == '/':
                    res = int(a / b)
                s.append(res)
            else:
                s.append(int(t))
        return s.pop()




# https://leetcode.com/problems/evaluate-reverse-polish-notation/description/
