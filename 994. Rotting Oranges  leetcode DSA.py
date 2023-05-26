# https://leetcode.com/problems/rotting-oranges/
def orangesRotting(self, grid: List[List[int]]) -> int:
from typing import List
from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        fresh_count = 0
        rotten = deque()
        minutes = 0
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    fresh_count += 1
                elif grid[i][j] == 2:
                    rotten.append((i, j, minutes))
        
        while rotten:
            x, y, minutes = rotten.popleft()
            
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                
                if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == 1:
                    grid[nx][ny] = 2
                    fresh_count -= 1
                    rotten.append((nx, ny, minutes + 1))
        
        return minutes if fresh_count == 0 else -1
