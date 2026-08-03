class Solution:
    def generate(self, n: int) -> List[List[int]]:
        grid=[]
        for i in range(n):
            grid.append([0]*(i+1))
    
        
        grid[0][0]=1
        for i in range(n):
            for j in range(i+1):
                if i==j==0:
                    continue
                val=0
                if j ==i:
                    grid[i][j]=1
                    continue
                if i>0:
                    val+=grid[i-1][j]
                if j>0:
                    val+=grid[i-1][j-1]
                grid[i][j]=val
        return grid
