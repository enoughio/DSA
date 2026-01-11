class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        row_len = len(matrix)
        temp = [ [0  for i in range(row_len)] for i in range(row_len) ]

        for i in range(row_len) :
            for j in range(i, row_len) :
                matrix[i][j], matrix[j][i] = matrix[j][i],matrix[i][j] 
            
            matrix[i].reverse()
    
        

