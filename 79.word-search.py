#
# @lc app=leetcode id=79 lang=python3
#
# [79] Word Search
#

# @lc code=start
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not board:
            return False
        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.dfs(board, i, j, word,0):
                    return True
        return False
    def dfs(self,board,i,j,word,index):
        if index == len(word):
            return True
        
        if i<0 or i >= len(board) or j < 0 or j >= len(board[0]) or index > len(word) or word[index]!=board[i][j]:
            return False
        
        
        temp = board[i][j] 
        board[i][j] = "#" 
        res = self.dfs(board,i-1,j,word,index+1) or  self.dfs(board,i+1,j,word,index+1) or self.dfs(board,i,j-1,word,index+1) or self.dfs(board,i,j+1,word,index+1)
        board[i][j] = temp
        return res
        
# @lc code=end

