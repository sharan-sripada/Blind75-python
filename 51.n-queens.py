#
# @lc app=leetcode id=51 lang=python3
#
# [51] N-Queens
#

# @lc code=start
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        ans =[]
        board=[["."]*n for _ in range(n)]
        col=set()
        pDiag=set()
        nDiag=set()
        
        def helper(r):
            if r==n:
                ans.append(["".join(row) for row in board])
                return
            for i in range(n):
                if i in col or (r+i) in nDiag or r-i in pDiag:
                    continue

                board[r][i]="Q"
                col.add(i)
                pDiag.add(r-i)
                nDiag.add(r+i)

                helper(r+1)

                board[r][i]="."
                col.remove(i)
                pDiag.remove(r-i)
                nDiag.remove(r+i)
        helper(0)
        return ans
                
                
            
                
                
        
    
        
# @lc code=end

