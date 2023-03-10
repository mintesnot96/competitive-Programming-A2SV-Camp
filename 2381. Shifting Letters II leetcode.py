class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        shifted_chars = []
        current_shift = 0
        timeline = [0] * (len(s) + 1)
        for start_index, end_index, shift_direction in shifts:
            diff = 1 if shift_direction else -1
            timeline[start_index] += diff
            timeline[end_index + 1] -= diff
        for i, char in enumerate(s):
            current_shift = (current_shift + timeline[i]) % 26
            char_num = ord(char) - ord('a')
            shifted_num = (char_num + current_shift) % 26
            shifted_char = chr(ord('a') + shifted_num)
            shifted_chars.append(shifted_char)
        return ''.join(shifted_chars)

      
      
      
      
# https://leetcode.com/problems/shifting-letters-ii/description/
