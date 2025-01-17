def isSubsequence(s, t) -> bool:
        if len(s) == 0:
            return True
        s_index = 0
        for i in t:
            if i in s:
                if s[s_index] == i:
                    s_index += 1
        print(s_index)
        print(len(s))
        if s_index == len(s):
            return True
        else:
            return False
print(isSubsequence("ab","baab"))