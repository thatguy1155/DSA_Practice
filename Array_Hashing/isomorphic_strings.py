class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_dict = {}
        t_dict = {}
        num_counter = 0
        for i in s:
            if i not in s_dict:
                num_counter += 1
                s_dict[i] = num_counter
        num_counter = 0
        for j in t:
            if j not in t_dict:
                num_counter += 1
                t_dict[j] = num_counter
        for x in range(len(s)):
            if t_dict[t[x]] == s_dict[s[x]]:
                continue
            else:
                return False
        return True
        