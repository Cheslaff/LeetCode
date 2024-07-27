class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    r = 0
                    c = 0

                    while c < len(matrix[0]):
                        if matrix[i][c] != 0:
                            matrix[i][c] = 'x'
                        c += 1

                    while r < len(matrix):
                        if matrix[r][j] != 0:
                            matrix[r][j] = 'x'
                        r += 1
        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 'x':
                    matrix[i][j] = 0
