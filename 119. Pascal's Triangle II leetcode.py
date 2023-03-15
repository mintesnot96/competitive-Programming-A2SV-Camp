class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex==0:
            return [1]
        prev=self.getRow(rowIndex-1)
        crr=[1]
        for i in range(len(prev)-1):
            crr.append(prev[i]+prev[i+1])
        crr.append(1)
        return crr


# https://leetcode.com/problems/pascals-triangle-ii/
