class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid: return 0
        visited = set()

        def dfs(i, j):
            if (i >= len(grid) or j >= len(grid[0]) or 
                i < 0 or j < 0 or grid[i][j] == 0 or (i, j) in visited):
                return 0

            visited.add((i, j))
            area = 1 + dfs(i + 1, j) + dfs(i, j + 1) + dfs(i - 1, j) + dfs(i, j - 1)
            return area

        area = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                area = max(area, dfs(i, j))

        return area