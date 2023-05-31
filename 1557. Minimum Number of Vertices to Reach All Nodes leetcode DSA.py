class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:

        inDegree = [0] * n

        for _, v in edges:
            inDegree[v] += 1

        return [i for i, d in enumerate(inDegree) if d == 0]
# https://leetcode.com/problems/minimum-number-of-vertices-to-reach-all-nodes/description/
