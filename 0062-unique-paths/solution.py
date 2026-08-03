class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        grid=[]
        for i in range(m):
            grid.append([0]*n)
        
        grid[0][0]=1
        for i in range(m):
            for j in range(n):
                if i==j==0:
                    continue
                val=0
                if i>0:
                    val+=grid[i-1][j]
                if j>0:
                    val+=grid[i][j-1]
                grid[i][j]=val
        return grid[m-1][n-1]
