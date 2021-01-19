class Solution:
    def romanToInt(self, s: str) -> int:
        
        numeral = { 'I': 1,
                    'V': 5,
                    'X': 10,
                    'L': 50,
                    'C': 100,
                    'D': 500,
                    'M': 1000, 
                    ' ': 0}
        
        characters = [char for char in s]
        characters += [' ']
        num = 0
        
        for i in range(len(characters)):
            
            if (characters[i] == ' '):
                break
                
            elif (characters[i] == 'I' and (characters[i + 1] == 'V' or characters[i + 1] == 'X')):
                num -= numeral[characters[i]]
                
            elif (characters[i] == 'X' and (characters[i + 1] == 'L' or characters[i + 1] == 'C')):
                num -= numeral[characters[i]]
                
            elif (characters[i] == 'C' and (characters[i + 1] == 'D' or characters[i + 1] == 'M')):
                num -= numeral[characters[i]]
                
            else:
                num += numeral[characters[i]]
            
        return(num)