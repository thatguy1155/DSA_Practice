class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])

        def dfs(i, j):
            #first part marks the bounds of the graph, super important
            if i < 0  or i >= m or j < 0 or j >= n or grid[i][j] != "1":
                return
            else:
                grid[i][j] = "0"
                dfs(i, j+1)
                dfs(i, j-1)
                dfs(i + 1,j)
                dfs(i - 1,j)
        num_islands = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    num_islands += 1
                    dfs(i, j)
        return num_islands

# good example of how to use dfs in function without scoping issue


class Too_Much_Memory_Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0
        for i,x in enumerate(grid):
            for j in range(len(x)):
                if grid[i][j] == "1":
                    islands += 1
                    isl = deque([[i,j]])
                    while len(isl) > 0:
                        sand = isl.popleft()
                        if sand[0] < len(grid) - 1:
                            if grid[sand[0] + 1][sand[1]] == "1":
                                isl.append([sand[0] + 1,sand[1]])
                        if sand[1] < len(grid[0]) - 1:
                            if grid[sand[0]][sand[1] + 1] == "1":
                                isl.append([sand[0],sand[1] + 1])
                        if sand[1] > 0:
                            if grid[sand[0]][sand[1] - 1] == "1":
                                isl.append([sand[0],sand[1] - 1])
                        if sand[0] > 0:
                            if grid[sand[0] - 1][sand[1]] == "1":
                                isl.append([sand[0] - 1,sand[1]])
                        grid[sand[0]][sand[1]] = "0"
        return islands