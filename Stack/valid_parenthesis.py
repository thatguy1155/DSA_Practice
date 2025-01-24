class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False
        parenthesis_pair = {
            ")": "(",
            "}": "{",
            "]": "[",
        }
        stack = []
        i = 0
        while i < len(s):
            if s[i] in parenthesis_pair.values():
                stack.append(s[i])
            if s[i] in parenthesis_pair.keys():
                if len(stack) == 0:
                    return False
                if stack[-1] == parenthesis_pair[s[i]]:
                    stack.pop()
                else:
                    return False
            i += 1

        if len(stack) == 0:
            return True
        return False
            
        
#best solution

class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = []
        mapping = {
            ')':'(',
            '}':'{', 
            ']':'['}
        
        for i in s:
            if i in mapping:
                if not stack or stack[-1] != mapping[i]:
                    return False
                stack.pop()
            else:
                stack.append(i)
            

        if not stack:
            return True
        else:
            return False