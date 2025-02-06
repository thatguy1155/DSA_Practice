class Solution:
    def isPalindrome(self, x: int) -> bool:
        str_x = str(x)
        if str_x[0] == "-":
            return False
        l = len(str_x)
        for i in range(l - 1):
            if str_x[i] != str_x[l - 1 - i]:
                return False
        return True
        
class BetterSolution:
    def isPalindrome(self, x: int) -> bool:
        x_str = str(x)
        return x_str == x_str[::-1] #this returns a backwards copy of the original string
    