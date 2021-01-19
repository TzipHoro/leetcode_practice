class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        
        m = len(accounts)
        n = len(accounts[0])
        wealth = [None] * m
                
        for i in range(m):
            
            total = 0
            
            for j in range(n):
            
                total += accounts[i][j]
            
            wealth[i] = total
            
        return(max(wealth))