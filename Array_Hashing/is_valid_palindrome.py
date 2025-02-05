def isPalindrome(self, s: str) -> bool:
        lowerchar = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","0","1","2","3","4","5","6","7","8","9"]
        list_s = list(s)
        
        fixed_str = [ch.lower() for ch in list(s) if ch.lower() in lowerchar]
        if len(fixed_str) == 0:
            return True
        
        p1 = 0
        p2 = len(fixed_str) - 1
        print(fixed_str)
        while p1 != p2 and p1 < len(fixed_str) - 1:
            if fixed_str[p1] != fixed_str[p2]:
                return False
            p1 += 1
            p2 -= 1
        return True
class BetterSolution:
    def isPalindrome(self, s: str) -> bool:
        clean = [char for char in list(s.lower()) if char.isalnum()]
        l = len(clean)
        for i in range(l-1):
            if clean[i] != clean[l-1-i]:
                return False
        return True