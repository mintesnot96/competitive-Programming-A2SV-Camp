# https://leetcode.com/problems/flood-fill/
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        if image[sr][sc] == newColor:
            return image
        
        visited = set()
        queue = [(sr, sc)]
        color = image[sr][sc]
        while queue:
            r, c = queue.pop(0)
            if (r, c) in visited or r < 0 or r >= len(image) or c < 0 or c >= len(image[0]) or image[r][c] != color:
                continue
            
            visited.add((r, c))
            queue.append((r-1, c)) # top neighbor
            queue.append((r+1, c)) # bottom neighbor
            queue.append((r, c-1)) # left neighbor
            queue.append((r, c+1)) # right neighbor
        
        for r, c in visited:
            image[r][c]= newColor
        
        return image
