class Solution:
    def isValid(self, s: str) -> bool:
        pars = {"{": "}", "(": ")", "[": "]"}
        stack = []
        for sign in s:
            if sign in pars:
                stack.append(sign)
            elif (len(stack) == 0) or (sign not in pars and pars[stack.pop()] != sign):
                return False
        
        return len(stack) == 0
            
