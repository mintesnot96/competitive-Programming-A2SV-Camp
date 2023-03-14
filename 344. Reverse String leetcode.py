class Solution:
    def reverseString(self, s: List[str]) -> None:
        left = 0
        right = len(s) - 1
        def recurhelper(left,right):
            s[left], s[right] = s[right], s[left]
            print(left,' ',right)
            left += 1
            right -= 1
            if left < right:
                recurhelper(left,right)

            return s
        recurhelper(left,right)

# class Solution:
#     def reverseString(self, s: List[str]) -> None:
        # left = 0
        # right = len(s) - 1
        # while left < right:
        #     s[left], s[right] = s[right], s[left]
        #     left += 1
        #     right -= 1



# https://leetcode.com/problems/reverse-string/
