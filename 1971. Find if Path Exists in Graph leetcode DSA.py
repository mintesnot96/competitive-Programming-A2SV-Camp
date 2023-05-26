class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
            # Step 1: Create adjacency list
        adjList = [[] for _ in range(n)]
        for edge in edges:
            u, v = edge
            adjList[u].append(v)
            adjList[v].append(u)

        # Step 2: DFS traversal
        visited = [False] * n

        def dfs(curr):
            visited[curr] = True
            if curr == destination:
                return True
            for neighbor in adjList[curr]:
                if not visited[neighbor]:
                    if dfs(neighbor):
                        return True
            return False

        return dfs(source)

# https://leetcode.com/problems/find-if-path-exists-in-graph/description/
