class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest_str = 0
        sub_str = ""
        char_dict = {}
        for index,ch in enumerate(s):
            if ch in char_dict and ch in sub_str:
                if len(sub_str) > longest_str:
                    longest_str = len(sub_str)
                sub_str = s[(char_dict[ch] + 1):index]
            char_dict[ch] = index
            sub_str += ch
        if len(sub_str) > longest_str:
            longest_str = len(sub_str)
        return longest_str
