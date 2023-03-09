class NumMatrix:
    def __init__(self, mat: List[List[int]]):
        if not mat:
            return
        m, n = len(mat), len(mat[0])
        self.s = [[0] * (n+1) for _ in range(m+1)]
        for i in range(1, m+1):
            for j in range(1, n+1):
                self.s[i][j] = mat[i-1][j-1] + self.s[i][j-1] + self.s[i-1][j] - self.s[i-1][j-1]

    def sumRegion(self, r1: int, c1: int, r2: int, c2: int) -> int:
        return self.s[r2+1][c2+1] - self.s[r1][c2+1] - self.s[r2+1][c1] + self.s[r1][c1]
# https://leetcode.com/problems/range-sum-query-2d-immutable/description/
