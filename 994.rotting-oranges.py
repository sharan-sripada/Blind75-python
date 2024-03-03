#
# @lc app=leetcode id=994 lang=python3
#
# [994] Rotting Oranges
#

# @lc code=start
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ans = 0

        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    steps = self.bfs(grid,i,j)
                    if steps == -1:
                        return -1
                    ans =max(ans,steps)
        
        return ans 
                    
    def bfs(self,grid,i,j):
        visited = [[0 for _ in range(len(grid[0]))] for _ in range(len(grid))]
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        queue = deque([(i,j,0)])
        
        while queue:
            curr_i, curr_j, steps = queue.popleft()
            visited[curr_i][curr_j] = 1
            if grid[curr_i][curr_j]==2:
                print(steps)
                return steps
            if grid[curr_i][curr_j]==0:
                continue
            
            for dx, dy in directions:
                new_i, new_j = curr_i+dx,curr_j+dy
                if self.is_valid(visited,new_i,new_j,len(grid),len(grid[0])):
                    queue.append((new_i,new_j,steps+1))
        return -1
    
    
    def is_valid(self, visited, x, y, rows, cols):
        return  0 <= x < rows and 0 <= y < cols and visited[x][y] ==0 
                
        
        
# @lc code=end

