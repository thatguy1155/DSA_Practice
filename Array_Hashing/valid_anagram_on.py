class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        w_dict = {}
        anagram_flag = True
        for i in s:
            if i not in w_dict:
                w_dict[i] = [1]
            else:
                w_dict[i][0] += 1
        for j in t:
            if j not in w_dict:
                return False
            else:
                if len(w_dict[j]) == 1:
                    w_dict[j].append(1)
                else:
                     w_dict[j][1] += 1
        for value in w_dict.values():
            if len(value) == 1:
                return False
            elif value[0] != value[1]:
                return False
        return True
    
    
