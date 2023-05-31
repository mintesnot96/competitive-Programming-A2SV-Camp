# https://leetcode.com/problems/maximal-network-rank/description/
class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        g = defaultdict(list)
        for i in roads:
            g[i[0]].append(i[1])
            g[i[1]].append(i[0])
        
        ans = 0
        for i in range(n - 1):
            for j in range(i + 1, n):
                if j in g[i]:
                    ans = max(ans, len(g[i]) + len(g[j]) - 1)
                else:
                    ans = max(ans, len(g[i])+ len(g[j]))
        
        return ans
