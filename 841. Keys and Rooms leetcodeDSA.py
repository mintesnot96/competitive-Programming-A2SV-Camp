# https://leetcode.com/problems/keys-and-rooms/
class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        n = len(rooms)
        visited = set()

        def dfs(room: int) -> None:
            visited.add(room)
            for key in rooms[room]:
                if key not in visited:
                    dfs(key)

        dfs(0)
        return len(visited) == n
