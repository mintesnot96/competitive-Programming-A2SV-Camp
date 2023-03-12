class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        c=0
        while tickets[k]!=0:
            for i in range(len(tickets)):
                if tickets[i]!=0 and tickets[k]!=0:
                    tickets[i]=tickets[i]-1
                    c+=1
        return c



# https://leetcode.com/problems/time-needed-to-buy-tickets/description/
