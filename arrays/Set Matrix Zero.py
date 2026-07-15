
from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        if not matrix or len(matrix[0])==0: return matrix
        row,col=len(matrix),len(matrix[0])
        flagR=any(matrix[0][i]==0 for i in range(col))
        flagC=any(matrix[i][0]==0 for i in range(row))
        for i in range(1,row):
            for j in range(1,col):
                if matrix[i][j]==0:
                    matrix[i][0]=0
                    matrix[0][j]=0
                    
        for i in range(1,row):
            for j in range(1,col):
                if matrix[0][j]==0 or matrix[i][0]==0:
                    matrix[i][j]=0
        if flagR:
            for i in range(col):
                matrix[0][i]=0
        if flagC:
            for i in range(row):
                matrix[i][0]=0
         
        return matrix
# Driver code
matrix = [[0,1,2,6],[3,0,5,2],[1,3,2,5]]
Solution().setZeroes(matrix)
for row in matrix:
    print(row)
