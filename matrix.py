import numpy as np
class Solution(object):
    def matrixBlockSum(self, mat, K):
        res = [[0] * len(mat[0]) for _ in mat]
        grid = [[0] * len(mat[0]) for _ in mat]
        for i in range(len(mat)):
            count = 0
            for j in range(len(mat[0])):
                count += mat[i][j]
                grid[i][j] = count

        for i in range(len(res)):
            for j in range(len(res[i])):
                left = max(0,j-K)
                right = min(j+K,len(res[i])-1)
                count = 0
                for row in range(max(0,i-K),min(i+K+1,len(res))):
                    if left == 0:
                        count += grid[row][right]
                    else:
                        count += (grid[row][right] - grid[row][left-1])
                res[i][j] = count
        return res
val=Solution()
n,k=map(int,input().split())
R=n
C=n
nums=list(map(int,input().split()))
matrix=np.array(nums).reshape(R,C)
print(*val.matrixBlockSum(matrix,k))
