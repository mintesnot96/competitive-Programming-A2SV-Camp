class NumMatrix:
    def __init__(self, mat: List[List[int]]):
        if not mat:
            return
        m, n = len(mat), len(mat[0])
        self.cumulative_sums = [[0] * n for _ in range(m)]
        self.cumulative_sums[0][0] = mat[0][0]
        # Compute cumulative sums for the first row and column
        for i in range(1, m):
            self.cumulative_sums[i][0] = self.cumulative_sums[i-1][0] + mat[i][0]
        for j in range(1, n):
            self.cumulative_sums[0][j] = self.cumulative_sums[0][j-1] + mat[0][j]
        # Compute cumulative sums for the rest of the matrix
        for i in range(1, m):
            for j in range(1, n):
                self.cumulative_sums[i][j] = self.cumulative_sums[i-1][j] + self.cumulative_sums[i][j-1] - self.cumulative_sums[i-1][j-1] + mat[i][j]

    def sumRegion(self, r1: int, c1: int, r2: int, c2: int) -> int:
        if r1 == 0 and c1 == 0:
            return self.cumulative_sums[r2][c2]
        elif r1 == 0:
            return self.cumulative_sums[r2][c2] - self.cumulative_sums[r2][c1-1]
        elif c1 == 0:
            return self.cumulative_sums[r2][c2] - self.cumulative_sums[r1-1][c2]
        else:
            return self.cumulative_sums[r2][c2] - self.cumulative_sums[r1-1][c2] - self.cumulative_sums[r2][c1-1] + self.cumulative_sums[r1-1][c1-1]
# https://leetcode.com/problems/range-sum-query-2d-immutable/description/
