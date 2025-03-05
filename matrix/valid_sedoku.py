class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        b_map = {}
        for i in range(9):
            for j in range(9):
                square = ""
                if (0 <= i <= 2) and (0 <= j <= 2):
                    square = "sq1"
                elif (0 <= i <= 2) and (3 <= j <= 5):
                    square = "sq2"
                elif (0 <= i <= 2) and (6 <= j <= 8):
                    square = "sq3"
                elif (3 <= i <= 5) and (0 <= j <= 2):
                    square = "sq4"
                elif (3 <= i <= 5) and (3 <= j <= 5):
                    square = "sq5"
                elif (3 <= i <= 5) and (6 <= j <= 8):
                    square = "sq6"
                elif (6 <= i <= 8) and (0 <= j <= 2):
                    square = "sq7"
                elif (6 <= i <= 8) and (3 <= j <= 5):
                    square = "sq8"
                elif (6 <= i <= 8) and (6 <= j <= 8):
                    square = "sq9"
                if board[i][j] != ".":
                    val = board[i][j]
                    if val not in b_map:
                        b_map[val] = {"v":[i],"h":[j],"sq":[square]}
                    else:
                        if i in b_map[val]["v"]:
                            return False
                        else:
                            b_map[val]["v"].append(i)
                        if j in b_map[val]["h"]:
                            return False
                        else:
                            b_map[val]["h"].append(j)
                        if square in b_map[val]["sq"]:
                            return False
                        else:
                            b_map[val]["sq"].append(square)
        return True