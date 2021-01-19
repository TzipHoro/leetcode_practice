class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        plus1 = digits
        
        for i in range(1, len(digits) + 1):
            
            if (digits[-i] != 9):
            
                plus1[-i] += 1
                return(plus1)
            
            else:
                plus1[-i] = 0
        
        if (plus1[-i] == 0):
            plus1 = [1] + plus1
            
        return(plus1)