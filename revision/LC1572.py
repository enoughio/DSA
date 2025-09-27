class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        
        n = len(mat)
        sum = 0

        for i in range(n) :
            sum += mat[i][i] 

        for i in range(n-1,-1,-1) :
            sum += mat[i][n-i-1]    

        if (n/2) > (n//2) :
            return sum  - mat[n//2][n//2]

        return sum