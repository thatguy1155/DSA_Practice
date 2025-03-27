#video solution

class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        length = len(board)
        board.reverse()
        def intToPos(square):
            r = (square - 1) // length
            c = (square - 1) % length
            if r % 2:
                c= length - 1 - c
            return [r,c]
        q = deque()
        q.append([1,0])
        visit = set()
        while q:
            square, moves = q.popleft()
            for i in range(1,7):
                nextSquare = square + i
                r, c = intToPos(nextSquare)
                if board[r][c] != -1:
                    nextSquare = board[r][c]
                if nextSquare == length * length:
                    return moves + 1
                if nextSquare not in visit:
                    visit.add(nextSquare)
                    q.append([nextSquare, moves + 1])
        return -1
            



#2nd attempt
class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        board_dict = {}
        direction = "back"
        counter = (len(board))**2
        if (len(board))**2 < 6:
            return 1
        for i,x in enumerate(board):
            if direction == "back":
                for j in range(len(board) - 1,-1,-1):
                    board_dict[counter] = x[j]
                    counter -= 1
                direction = "forward"
            else:
                for j in range(len(board)):
                    board_dict[counter] = x[j]
                    counter -= 1
                direction = "back"
        game = deque([[1,0]])
        position = 1
        while position != (len(board))**2:
            curr_pos = game.popleft()
            position = curr_pos[0]
            curr_role = curr_pos[1]
            print(position)
            print(curr_role)
            #if curr_role >= (len(board)**2 - 6):
                #return curr_role + 1
            for i in range(position + 1,position + 7):
                if i <= len(board)**2:
                    if board_dict[i] > 0:
                        game.append([board_dict[i],curr_role + 1])
                    elif board_dict[position] == -1:
                        game.append([i,curr_role + 1])
                    board_dict[i] == -2
        return curr_role

        
            
        print(board_dict)
            



#1st Attempt
class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        board_dict = {}
        direction = "back"
        counter = (len(board))**2
        if (len(board))**2 < 6:
            return 1
        for i,x in enumerate(board):
            if direction == "back":
                for j in range(len(board) - 1,-1,-1):
                    board_dict[counter] = x[j]
                    counter -= 1
                direction = "forward"
            else:
                for j in range(len(board)):
                    board_dict[counter] = x[j]
                    counter -= 1
                direction = "back"
        def dfs(space, dice_count):
            print(space)
            print(dice_count)
            print("-_-_-_-_")
            if space == (len(board))**2:
                return 0
            if space >= (len(board))**2 - 6:
                return 1
            if board_dict[space] == -2:
                return 999999999
            if board_dict[space] > 0:
                new_count = dfs(board_dict[space],dice_count + 1)
                board_dict[space] = -2
                return dice_count + new_count
            else:
                min_path = 999999999
                for i in range(space + 1,space + 7):
                    path_count = dfs(i,dice_count + 1)
                    board_dict[i] = -2
                    if path_count < min_path:
                        min_path = path_count
                return path_count + min_path
        count = dfs(1,0)
        if count == 999999999:
            return -1
        else:
            return count
            
        print(board_dict)
            
