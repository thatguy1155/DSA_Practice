class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        note = True
        zine_dict = {}
        for i in magazine:
            if i in zine_dict:
                zine_dict[i] += 1
            else:
                zine_dict[i] = 1

        for j in ransomNote:
            if j in zine_dict:
                zine_dict[j] -= 1
                
            else:
                return False
            if zine_dict[j] < 0:
                    return False
            
        return True
        
#Best Solution
    class Solution:
      def canConstruct(self, ransomNote: str, magazine: str) -> bool:
          for i in ransomNote:
              if i in magazine:
                  magazine = magazine.replace(i, "", 1)
              else:
                  return False
          return True