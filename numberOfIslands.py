class Solution:
    
    #Function to find the number of islands.
    def solve(self, i, j, R, C, grid):
        if not (0 <= i < R) or not (0 <= j < C):
            return
            
        elif grid[i][j] == "0":
            return
            
            
        
        grid[i][j] = "0"
        
        directions = [[-1, -1], [-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [1, -1], [0, -1]]
        
        for d in directions:
            self.solve(i + d[0], j + d[1], R, C, grid)
            
            
    def numIslands(self, grid):
		#Code here
        R = len(grid)
        C = len(grid[0])
        count = 0
        
        for i in range(R):
            for j in range(C):
                if grid[i][j] != "0":
                    self.solve(i, j, R, C, grid)
                    count += 1
                    
        
        return count