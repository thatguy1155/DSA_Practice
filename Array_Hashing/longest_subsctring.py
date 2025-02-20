def longestSubstring(self, strs: List[str]) -> str:
        char_dict = {}
        string = ""
        longest_string = ""

        for st in strs:
            for index,ch in enumerate(st):
                if str(index) + ch in char_dict:
                    char_dict[str(index) + ch] += 1
                else:
                    char_dict[str(index) + ch] = 1

        print(char_dict)
        for k in char_dict.keys():
            if char_dict[k] == len(strs):
                string += k[1]
                if len(string) > len(longest_string):
                    longest_string = string
            else:
                string = ""
        return longest_string