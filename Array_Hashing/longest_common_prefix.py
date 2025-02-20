class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        char_dict = {}
        string = ""
        longest_string = ""

        for st in strs:
            for index,ch in enumerate(st):
                if str(index) + ch in char_dict:
                    char_dict[str(index) + ch] += 1
                else:
                    char_dict[str(index) + ch] = 1

        index = 0
        for k in char_dict.keys():
            if char_dict[k] == len(strs) and int(k[:-1]) == index:
                string += k[-1]
                index += 1
            else:
                return string
        return string

# better solution
    
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        
        strs.sort()        
        first, last = strs[0], strs[-1]
        prefix = []        
        for i in range(min(len(first), len(last))):
            if first[i] == last[i]:
                prefix.append(first[i])
            else:
                break  
        
        return "".join(prefix)