https://leetcode.com/problems/max-area-of-island/description/
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def dfs(grid, r, c, area):
            if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]) or grid[r][c] != 1:
                return 0
            
            grid[r][c] = 2
            area += 1
            area += dfs(grid, r-1, c, 0) # top neighbor
            area += dfs(grid, r+1, c, 0) # bottom neighbor
            area += dfs(grid, r, c-1, 0) # left neighbor          
            area += dfs(grid, r, c+1, 0) # right neighbor
            return area
        
        max_area = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    max_area = max(max_area, dfs(grid, r, c, 0))
        
        return max_area
