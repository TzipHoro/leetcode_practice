class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        
        first = ''
        second = ''
        
        for i in word1:
            
            first += i
            
        for i in word2:
            
            second += i
            
        return(first == second)