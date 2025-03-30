class Solution:
    def reverseWords(self, s: str) -> str:
        s_arr = s.split(' ')
        s_arr = [x for x in s_arr if x is not '']
        s_arr.reverse()
        return (' ').join(s_arr)