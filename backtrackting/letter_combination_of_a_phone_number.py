class Solution:
    def __init__(self):
        self.phone_dict = {
            "2": ["a","b","c"],
            "3": ["d","e","f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m","n","o"],
            "7": ["p","q","r","s"],
            "8": ["t","u","v"],
            "9": ["w","x","y","z"]
        }
    def combineArrays(self,digitarr: List[str],num: str)-> List[str]:
        if digitarr == []:
            if num == "7" or num == "9":
                digitarr = [[], [], [], []]
            else:
                digitarr = [[], [], []]
        else:
            digitarr = [digitarr for _ in range(len(self.phone_dict[num]))]
        for i in range(len(digitarr)):
            if digitarr[i] == []:
                digitarr[i] = [self.phone_dict[num][i]]
            else:
                digitarr[i] = [x + self.phone_dict[num][i] for x in digitarr[i]]
        flattened = [item for row in digitarr for item in row]
        return flattened
        
    def letterCombinations(self, digits: str) -> List[str]:
        answer = []
        if len(digits) == 0:
            return answer
        for k in digits:
            answer = self.combineArrays(answer,k)
        return answer

        