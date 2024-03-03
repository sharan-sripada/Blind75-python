 #
# @lc app=leetcode id=542 lang=python3
#
# [542] 01 Matrix
#

# @lc code=start
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:

        m,n=len(mat),len(mat[0])
        
        for i in range(0,m):
            for j in range(0,n):
                if mat[i][j]>0:
                    t=mat[i-1][j] if i>0  else math.inf
                    l=mat[i][j-1] if j>0 else math.inf
                    mat[i][j]=min(t,l)+1
        
        for i in range(m-1,-1,-1):
            for j in range(n-1,-1,-1):
                if mat[i][j]>0:
                    d=mat[i+1][j] if i+1<m  else math.inf
                    r=mat[i][j+1] if j+1<n else math.inf
                    mat[i][j]=min(mat[i][j],d+1,r+1)
        return mat
# @lc code=end

