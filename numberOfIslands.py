class Solution:
    def numIslands(self, grid: List[List[str]]) -> int: 
        
        if not grid:
            return 0
        
        islands = 0 
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    self.dfs(grid, i, j)
                    islands += 1
        return islands
    
        
        
    def dfs(self, grid, i, j):
        if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] != '1':
            return
        else:
            grid[i][j] = '0'
            self.dfs(grid, i + 1, j)
            self.dfs(grid, i - 1, j)
            self.dfs(grid, i, j + 1)
            self.dfs(grid, i, j - 1)
            
    
    
obj = Solution()  
print(obj.numIslands([
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]))
print(obj.numIslands([
  ["0","0","0","0","0"],
  ["0","0","0","0","0"],
  ["0","0","0","0","0"],
  ["0","0","0","0","0"]
]))
print(obj.numIslands([]))
print(obj.numIslands([
  ["1","1","1","1","1"],
  ["1","1","1","1","1"],
  ["1","1","1","1","1"],
  ["1","1","1","1","1"]
]))
print(obj.numIslands([
  ["1","0","1","0","1"],
  ["0","1","0","1","0"],
  ["1","0","1","0","1"],
  ["0","1","0","1","0"]
]))
    