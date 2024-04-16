class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        pos = set()
        for i in range(len(matrix)):
            counter = matrix[i].count(0)
            j = 0
            while counter > 0:
                if matrix[i][j] == 0:
                    pos.add(j)
                    counter -= 1
                j += 1

        for i in range(len(matrix)):
            if matrix[i].count(0) > 0:
                matrix[i] = len(matrix[i]) * [0]
                continue
            for j in list(pos):
                matrix[i][j] = 0