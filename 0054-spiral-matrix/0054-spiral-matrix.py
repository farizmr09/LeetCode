class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        spiral = []
        try:
            while len(matrix):
                for i in matrix[0]:
                    spiral.append(i)
                matrix.remove(matrix[0])
                for i in range(len(matrix)):
                    spiral.append(matrix[i][-1])
                    matrix[i].remove(matrix[i][-1])
                for i in reversed(matrix[-1]):
                    spiral.append(i)
                matrix.remove(matrix[-1])
                for i in range(len(matrix) - 1, 0, -1):
                    spiral.append(matrix[i][0])
                    matrix[i].remove(matrix[i][0])
                
        except:
            pass
        
        return(spiral)