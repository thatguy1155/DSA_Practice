class Solution:
    def solve(self, board: List[List[str]]) -> None:
        m = len(board)
        n = len(board[0])

        def dfs(i,j):
            if i < 0 or i >= m or j < 0 or j >= n:
                return
            if board[i][j] != 'O':
                return
            
            board[i][j] = 'T'
            dfs(i + 1,j)
            dfs(i - 1,j)
            dfs(i,j + 1)
            dfs(i,j - 1)
            return


            
        for i in range(m):
            if board[i][0] == "O":
                dfs(i,0)
            if board[i][n-1] == "O":
                dfs(i,n-1)
        
        for j in range(n):
            if board[0][j] == "O":
                dfs(0,j)
            print(str(n-1))
            if board[m-1][j] == "O":
                dfs(m-1,j)
        
        print(str(board))
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'T':
                    board[i][j] = 'O'
                else:
                    board[i][j] = 'X'
            

            
        """
        Do not return anything, modify board in-place instead.
        """
        